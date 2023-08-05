import{b as e,d as t,n as o,s as i,y as a,h as n}from"./index-0718df31.js";import"./c.644c7642.js";import{d as l}from"./c.dd6ca16a.js";let d=class extends i{render(){return a`
      <mwc-dialog
        .heading=${`Delete ${this.name}`}
        @closed=${this._handleClose}
        open
      >
        <div>Are you sure you want to delete ${this.name}?</div>
        <mwc-button
          slot="primaryAction"
          label="Delete"
          dialogAction="close"
          @click=${this._handleDelete}
        ></mwc-button>
        <mwc-button
          slot="secondaryAction"
          no-attention
          label="Cancel"
          dialogAction="cancel"
        ></mwc-button>
      </mwc-dialog>
    `}_handleClose(){this.parentNode.removeChild(this)}async _handleDelete(){await l(this.configuration),n(this,"deleted")}};e([t()],d.prototype,"name",void 0),e([t()],d.prototype,"configuration",void 0),d=e([o("esphome-delete-device-dialog")],d);
