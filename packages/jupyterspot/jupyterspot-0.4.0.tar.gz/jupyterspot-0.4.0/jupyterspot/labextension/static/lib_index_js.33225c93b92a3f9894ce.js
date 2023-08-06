"use strict";
(self["webpackChunkjupyterspot"] = self["webpackChunkjupyterspot"] || []).push([["lib_index_js"],{

/***/ "./lib/index.js":
/*!**********************!*\
  !*** ./lib/index.js ***!
  \**********************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "ButtonExtension": () => (/* binding */ ButtonExtension),
/* harmony export */   "default": () => (__WEBPACK_DEFAULT_EXPORT__)
/* harmony export */ });
/* harmony import */ var _jupyterlab_settingregistry__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @jupyterlab/settingregistry */ "webpack/sharing/consume/default/@jupyterlab/settingregistry");
/* harmony import */ var _jupyterlab_settingregistry__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_settingregistry__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @jupyterlab/apputils */ "webpack/sharing/consume/default/@jupyterlab/apputils");
/* harmony import */ var _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__);
/* harmony import */ var _jupyterlab_coreutils__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! @jupyterlab/coreutils */ "webpack/sharing/consume/default/@jupyterlab/coreutils");
/* harmony import */ var _jupyterlab_coreutils__WEBPACK_IMPORTED_MODULE_2___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_coreutils__WEBPACK_IMPORTED_MODULE_2__);
/* harmony import */ var _lumino_disposable__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! @lumino/disposable */ "webpack/sharing/consume/default/@lumino/disposable");
/* harmony import */ var _lumino_disposable__WEBPACK_IMPORTED_MODULE_3___default = /*#__PURE__*/__webpack_require__.n(_lumino_disposable__WEBPACK_IMPORTED_MODULE_3__);





// local
// const backendURL = 'http://192.168.1.100:5000';
// const frontendURL = 'http://192.168.1.100:5420';
// prod
const backendURL = 'https://api.jupyterspot.com';
const frontendURL = 'https://jupyterspot.com';
let apiKey = '';
/**
 * Adds a notebook to JupyterSpot.
 */
async function addNotebook(panel, apiKey) {
    if (!apiKey) {
        (0,_jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__.showErrorMessage)('Your JupyterSpot API key has not been set.', 'Get your API key by going to https://jupyterspot.com/account, then add it to ' +
            'JupyterLab by going to Settings -> Advanced Settings Editor -> JupyterSpot ' +
            'and updating the API_KEY setting.');
        return;
    }
    // get JSON notebook representation from the panel
    if (!panel.content.model) {
        (0,_jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__.showErrorMessage)("Notebook has no content, can't add it to JupyterSpot.", '');
        return;
    }
    const nb_json = JSON.stringify(panel.content.model.toJSON(), null);
    // TODO: handle Windows paths
    const nb_path = _jupyterlab_coreutils__WEBPACK_IMPORTED_MODULE_2__.PageConfig.getOption('serverRoot') + '/' + panel.context.localPath;
    const requestUrl = backendURL + '/api/v1/convert-nb-from-json-ext';
    console.info('JupyterSpot requestUrl:', requestUrl);
    const fd = new FormData();
    fd.append('nb_json', nb_json);
    fd.append('api_key', apiKey);
    fd.append('path', nb_path);
    const dialogTitle = 'Adding notebook to JupyterSpot...';
    (0,_jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__.showErrorMessage)(dialogTitle, "You can dismiss this and continue working. Another dialog will show when it's done.");
    // get the open dialog and set it's content to `msg`
    function setMsg(msgHTML, msgPlain) {
        const dialogs = document.getElementsByClassName('jp-Dialog');
        if (dialogs.length > 0) {
            const dialog = dialogs[0];
            const msgDiv = dialog.getElementsByClassName('jp-Dialog-body')[0];
            msgDiv.innerHTML = msgHTML;
        }
        else {
            console.log('JupyterSpot: no open dialog found');
            (0,_jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__.showErrorMessage)(dialogTitle, msgPlain);
        }
    }
    await fetch(requestUrl, {
        method: 'post',
        body: fd
    })
        .then(res => res.json())
        .then(res => {
        console.log('JupyterSpot result:', res);
        if (res.success) {
            const url = frontendURL + '/notebook?id=' + res.id;
            window.open(url);
            const msgHTML = 'Added notebook to JupyterSpot successfully.  ' +
                "If a new tab didn't open, you may want to give your browser permission to open popups from JupyterLab. " +
                "The link to your notebook's whiteboard is: <a href='" +
                url +
                "' target='_blank'>" +
                url +
                '</a>';
            // no way to set HTML if dialog was closed
            const msgPlain = 'Added notebook to JupyterSpot successfully.  ' +
                "If a new tab didn't open, you may want to give your browser permission to open popups from JupyterLab. " +
                "The link to your notebook's whiteboard is: " +
                url;
            setMsg(msgHTML, msgPlain);
            console.info('JupyterSpot notebook url: ', url);
        }
        else {
            const msg = 'Error adding notebook to JupyterSpot: ' + res.msg;
            setMsg(msg, msg);
        }
        return res;
    })
        .catch(error => {
        console.log('JupyterSpot error:', error);
        const msg = 'Error adding the notebook to JupyterSpot: ' + error.toString();
        setMsg(msg, msg);
        return error;
    });
}
/**
 * A notebook widget extension that adds the open notebook to JupyterSpot.
 */
class ButtonExtension {
    /**
     * Create a new extension for the notebook panel widget.
     *
     * @param panel Notebook panel
     * @param context Notebook context
     * @returns Disposable on the added button
     */
    createNew(panel, context) {
        const button = new _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__.ToolbarButton({
            className: 'upload-button',
            label: 'Open in JupyterSpot',
            tooltip: 'Open in JupyterSpot',
            pressedTooltip: 'Adding notebook to JupyterSpot',
            disabledTooltip: 'Adding notebook to JupyterSpot...',
            enabled: true,
            pressed: false,
            onClick: () => addNotebook(panel, apiKey)
        });
        panel.toolbar.insertItem(10, 'openInJupyterSpot', button);
        return new _lumino_disposable__WEBPACK_IMPORTED_MODULE_3__.DisposableDelegate(() => {
            button.dispose();
        });
    }
}
/**
 * Initialization data for the jupyterspot extension.
 */
const plugin = {
    id: 'jupyterspot:plugin',
    autoStart: true,
    requires: [_jupyterlab_settingregistry__WEBPACK_IMPORTED_MODULE_0__.ISettingRegistry],
    activate: (app, settings) => {
        console.log('JupyterLab extension jupyterspot is activated!');
        // add the button
        app.docRegistry.addWidgetExtension('Notebook', new ButtonExtension());
        /**
         * Load the settings for this extension
         *
         * @param setting Extension settings
         */
        function loadSetting(setting) {
            // Read the settings and convert to the correct type
            apiKey = setting.get('API_KEY').composite;
            if (apiKey) {
                console.log('JupyterSpot apiKey is set');
            }
            else {
                console.log('JupyterSpot apiKey is NOT set');
            }
        }
        // Wait for the application to be restored and
        // for the settings for this plugin to be loaded
        Promise.all([app.restored, settings.load(plugin.id)])
            .then(([, setting]) => {
            // Read the settings
            loadSetting(setting);
            // Listen for your plugin setting changes using Signal
            setting.changed.connect(loadSetting);
        })
            .catch(reason => {
            console.error(`Something went wrong when reading the settings.\n${reason}`);
        });
    }
};
/* harmony default export */ const __WEBPACK_DEFAULT_EXPORT__ = (plugin);


/***/ })

}]);
//# sourceMappingURL=lib_index_js.33225c93b92a3f9894ce.js.map