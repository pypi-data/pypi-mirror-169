import os
import sys
from pathlib import Path

# from steam_sdk.data.DataAnalysis import ModifyModel, AddAuxiliaryFile
from steam_sdk.data.DataAnalysis import DataAnalysis
from steam_sdk.parsers.ParserYAML import yaml_to_data
from steam_sdk.parsers.ParserYAML import dict_to_yaml
from steam_sdk.analyses.AnalysisSTEAM import AnalysisSTEAM


class DriverAnalysis:

    def __init__(self, analysis_yaml_path: str = None):
        self.analysis_yaml_path = analysis_yaml_path
        self.analysis_data = yaml_to_data(analysis_yaml_path, DataAnalysis)
        path_dakota_python = os.path.join(Path(self.analysis_data.PermanentSettings.Dakota_path).parent.parent, 'share\dakota\Python')
        print('path_dakota_python:        {}'.format(path_dakota_python))
        sys.path.insert(0, path_dakota_python)
        from dakota.interfacing import read_parameters_file

        # Read DAKOTA parameters
        self.read_parameters_file = read_parameters_file

        # Initialize AnalysisSTEAM analysis
        self.analysis = AnalysisSTEAM(file_name_analysis=self.analysis_yaml_path, verbose=True)

    def prepare_analysis(self, params):
        variables = []
        values = []
        for var, value in params.items():
            variables.append(var)
            values.append(value)

        # type_sequence = [self.analysis_data.AnalysisStepDefinition[step].type
        #                  for step in self.analysis_data.AnalysisStepSequence]
        # runs = [i for i, x in enumerate(type_sequence) if x == 'RunSimulation']
        # last_make = len(type_sequence) - 1 - type_sequence[::-1].index('MakeModel')
        # last_modify = len(type_sequence) - 1 - type_sequence[::-1].index('ModifyModel')
        # last_modify_multiple = len(type_sequence) - 1 - type_sequence[::-1].index('ModifyModelMultipleVariables')
        # modified_step = self.analysis_data.AnalysisStepDefinition[self.analysis_data.AnalysisStepSequence[
        #     max(last_modify, last_modify_multiple)]]

        i = -1
        while (self.analysis_data.AnalysisStepDefinition[self.analysis_data.AnalysisStepSequence[i]].type
               not in ['ModifyModel', 'ModifyModelMultipleVariables']):
            i -= 1
        modified_step = self.analysis_data.AnalysisStepDefinition[self.analysis_data.AnalysisStepSequence[i]]

        if modified_step.type == 'ModifyModel':
            modified_step.variable_to_change = variables[0]
            modified_step.variable_value = values
        elif modified_step.type == 'ModifyModelMultipleVariables':
            modified_step.variables_to_change = variables
            modified_step.variables_value = [[value] for value in values]

        dict_to_yaml(self.analysis_data.dict(), self.analysis_yaml_path)

    def drive(self):
        params, result_for_dakota = self.read_parameters_file()  # inputs, outputs

        # Update analysis
        self.prepare_analysis(params)

        # Run the model
        self.analysis.run_analysis()

        # Write back to DAKOTA
        for i, label in enumerate(result_for_dakota):
            if result_for_dakota[label].asv.function:
                result_for_dakota[label].function = self.analysis.overall_parameter[label]

        result_for_dakota.write()
        return 1
