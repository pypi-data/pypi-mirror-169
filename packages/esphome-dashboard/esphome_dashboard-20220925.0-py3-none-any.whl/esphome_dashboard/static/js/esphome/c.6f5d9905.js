import{b as o,d as t,p as s,n as e,s as i,y as r,V as a}from"./index-0718df31.js";import"./c.eae257d9.js";import{o as n}from"./c.3271f53f.js";import"./c.644c7642.js";import"./c.8f86cda9.js";import"./c.1b7fdd9b.js";let c=class extends i{render(){return r`
      <esphome-process-dialog
        always-show-close
        .heading=${`Logs ${this.configuration}`}
        .type=${"logs"}
        .spawnParams=${{configuration:this.configuration,port:this.target}}
        @closed=${this._handleClose}
        @process-done=${this._handleProcessDone}
      >
        <mwc-button
          slot="secondaryAction"
          dialogAction="close"
          label="Edit"
          @click=${this._openEdit}
        ></mwc-button>
        ${void 0===this._result||0===this._result?"":r`
              <mwc-button
                slot="secondaryAction"
                dialogAction="close"
                label="Retry"
                @click=${this._handleRetry}
              ></mwc-button>
            `}
      </esphome-process-dialog>
    `}_openEdit(){a(this.configuration)}_handleProcessDone(o){this._result=o.detail}_handleRetry(){n(this.configuration,this.target)}_handleClose(){this.parentNode.removeChild(this)}};o([t()],c.prototype,"configuration",void 0),o([t()],c.prototype,"target",void 0),o([s()],c.prototype,"_result",void 0),c=o([e("esphome-logs-dialog")],c);
