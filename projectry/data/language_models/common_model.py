from builtins import staticmethod


class ProjectryObjectModel:
    @staticmethod
    def render(self, *args, **kwargs) -> str:
        pass


class FunctionModel(ProjectryObjectModel):
    pass


class ClassModel(ProjectryObjectModel):
    pass


class LanguageModel:
    function_model: FunctionModel = FunctionModel
    class_model: ClassModel = ClassModel
