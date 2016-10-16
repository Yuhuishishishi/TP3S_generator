class TP3SAnalyzer:
    def __init__(self, inst):
        """

        :type inst: analyzer.reader.Instance
        """
        self.inst = inst

    def test_dur_dist(self):
        prep = [t.prep for t in self.inst.test_arr]
        tat = [t.tat for t in self.inst.test_arr]
        analysis = [t.tat for t in self.inst.test_arr]
        dur = [t.dur for t in self.inst.test_arr]

        min_prep, max_prep, avg_prep = min(prep), max(prep), float(sum(prep))/len(prep)
        min_tat, max_tat, avg_tat = min(tat), max(tat), float(sum(tat))/len(tat)
        min_analysis, max_analysis, avg_analysis = min(analysis), max(analysis), float(sum(analysis))/len(analysis)
        min_dur, max_dur, avg_dur = min(dur), max(dur), float(sum(dur))/len(dur)

        print """Min prep: {min_prep}, Max prep: {max_prep}, Mean prep: {avg_prep}
                 Min tat: {min_tat}, Max tat: {max_tat}, Mean tat: {avg_tat}
                 Min analysis: {min_analysis}, Max analysis: {max_analysis}, Mean analysis: {avg_analysis}
                 Min dur: {min_dur}, Max dur: {max_dur}, Mean dur: {avg_dur}""".format(min_prep=min_prep,
                                                                                       max_prep=max_prep,
                                                                                       avg_prep=avg_prep,
                                                                                       min_tat=min_tat,
                                                                                       max_tat=max_tat,
                                                                                       avg_tat=avg_tat,
                                                                                       min_analysis=min_analysis,
                                                                                       max_analysis=max_analysis,
                                                                                       avg_analysis=avg_analysis,
                                                                                       min_dur=min_dur,
                                                                                       max_dur=max_dur,
                                                                                       avg_dur=avg_dur)

    def general_info(self):
        num_test = self.inst.num_test
        num_vehicle = self.inst.num_vehicle

        print "Num tests: {num_tests}\n Num vehicles: {num_vehicles}".format(num_tests=num_test,
                                                                             num_vehicles=num_vehicle)

    def vehicle_build_rate(self):
        pass

    def rehit_rule_analyze(self):
        pass





