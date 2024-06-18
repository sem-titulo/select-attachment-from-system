from odoo import models, fields, api
    
    
class IrAttachmentSelectFileWizardInherit(models.TransientModel):
    _name = "ir.attachment.select.files.wizard"
    
    
    ir_attachment_ids = fields.Many2many('ir.attachment', string='Anexos do Sistema')
    
    
    def action_save(self):

        # Postar a mensagem no chatter do registro com os arquivos como anexos
        record = self.env[self.env.context.get("res_model")].browse(int(self.env.context.get("res_id")))
        message = "Arquivos anexados: %s" % ', '.join([attachment.name for attachment in self.ir_attachment_ids])
        attachment_ids = [attachment.id for attachment in self.ir_attachment_ids]  # Lista de tuplas para adicionar os anexos
        record.message_post(attachment_ids=attachment_ids)

        # Retornar ação para recarregar a página
        return {
            'type': 'ir.actions.client',
            'tag': 'reload',
        }