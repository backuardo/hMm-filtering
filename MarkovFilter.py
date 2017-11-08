from RoboMaze import *
# MarkovFilter.py
# Eisner Nov 2017
#
# This class implements filtering on a RoboMaze object.


class MarkovFilter:
    def __init__(self, rm):
        """
        :param rm: RoboMaze object
        """
        self.rm = rm                        # RoboMaze object
        self.w = rm.w                       # Wall locations
        self.b = rm.b                       # Border locations
        self.maze = rm.maze                 # Maze in list form
        self.sequence = rm.sequence         # Ground truth sequence
        self.prior = self.generate_prior()  # Initial distribution

    def filter(self):
        """
        Calculates probability distribution for each step in a sequence

        :return: distribution in list form
        """
        states = [self.generate_prior()]
        distributions = []
        for i in range(len(self.sequence)):
            prediction = self.predict(states[i])
            update = self.update(prediction, i)
            normalized = self.normalize(update)
            states.append(normalized)

        for state in states:
            trunc = []
            for fl in state:
                trunc.append('%.4f' % fl)
            distributions.append(trunc)

        return distributions

    def predict(self, x):
        """
        Calculates probability distribution with evidence

        :param x: state
        :return: distribution in list form
        """
        # For maze index in state:
        for m_i in range(len(x)):
            m_p = []  # Probabilities for m_i's prediction
            if m_i not in self.b[0] and (m_i + 4) not in self.w:
                m_p.append(0.25)

            if m_i not in self.b[1] and (m_i - 4) not in self.w:
                m_p.append(0.25)

            if m_i not in self.b[2] and (m_i + 1) not in self.w:
                m_p.append(0.25)

            if m_i not in self.b[3] and (m_i - 1) not in self.w:
                m_p.append(0.25)

            t = 0

            for i in m_p:
                t += i

            m_p.append(1 - t) if t < 1 else m_p.append(1)
            for p in m_p:
                x[m_i] *= p
        return x

    def update(self, x, t):
        """
        Calculates probability distribution without evidence

        :param x: state
        :param t: evidence
        :return: distribution in list form
        """
        e = self.get_sensor_reading(t)
        # For maze index in state:
        for m_i in range(len(x)):
            if self.maze[m_i] == e:
                x[m_i] *= 0.88
            else:
                x[m_i] *= 0.04

        return x

    def generate_prior(self):
        """
        Calculates probability distribution at time 0

        :return: distribution in list form
        """
        possible = 1 / (16 - len(self.w))
        p = []

        for i in self.maze:
            p.append(0.0 if i == 'X' else possible)

        return p

    def get_sensor_reading(self, t):
        """
        Evaluates an imperfect sensor reading

        :param t: time step
        :return: a string representation of a color
        """
        c = {'r': 0.04,  # Initial reading probabilities
             'g': 0.04,
             'b': 0.04,
             'y': 0.04}

        gt = self.maze[self.sequence[t]]  # Ground truth
        c[gt] = 0.88  # Update probability for ground truth value
        i = random()

        c_list = [c['r'],
                  c['r'] + c['g'],
                  c['r'] + c['g'] + c['b'],
                  c['r'] + c['g'] + c['b'] + c['y']]

        if i < c_list[0]:
            return 'r'

        if i < c_list[1]:
            return 'g'

        if i < c_list[2]:
            return 'b'

        if i < c_list[3]:
            return 'y'

    @staticmethod
    def normalize(x):
        """
        Normalizes a probability distribution in list form
        Credit: Tony Suffolk 66 - https://stackoverflow.com/a/26785464
        :param x: probability before normalization
        :return: normalized probability distribution
        """
        return [float(i) / sum(x) for i in x]



