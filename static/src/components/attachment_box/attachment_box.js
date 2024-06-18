/** @odoo-module **/

import { AttachmentBox } from '@mail/components/attachment_box/attachment_box';
import { patch } from 'web.utils';

patch(AttachmentBox.prototype, 'owl/static/src/components/attachment_box/attachment_box.js', {
    _onClickAddAttachmentFromSystem(ev) {
        const currentUrl = window.location.href;
        const hashParams = new URLSearchParams(window.location.hash.replace('#', ''));
        const recordId = hashParams.get('id');
        const modelId = hashParams.get('model');

        this.env.bus.trigger('do-action', {
            action: {
                type: 'ir.actions.act_window',
                name: 'Anexos',
                res_model: 'ir.attachment.select.files.wizard',
                views: [[false, 'form']],
                target: 'new',
                context: { res_id: recordId, res_model: modelId}
            },
        });
    },
});
