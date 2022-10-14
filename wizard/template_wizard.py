from odoo import models,fields
import logging


_logger = logging.getLogger(__name__)


class TemplateWizard(models.TransientModel):
    _name = 'project.template.wizard'
    _description = 'Template Wizard'

    TEMPLATES = [
        ('rat','Risk Assessment Template')
    ]
    
    selection = fields.Selection(TEMPLATES,default=TEMPLATES[0][0],string="Project Type")
    project_name = fields.Char("Project Name",required=True)

    def create_project_template(self):
        project = self.env['project.project'].create({
            'name':self.project_name
        })

        _logger.info("Test " + str(project.id))

        self.env['project.task.type'].create({
            'name':"Column 1",
            'project_ids':[project.id]
        })
        return {
                'type': 'ir.actions.client',
                'tag': 'reload',
                }