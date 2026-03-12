class PromptBuilder:

    def __init__(self, template):
        self.template = template

    def build(self, query, context):
        return self.template.format(
            query=query,
            context=context
        )