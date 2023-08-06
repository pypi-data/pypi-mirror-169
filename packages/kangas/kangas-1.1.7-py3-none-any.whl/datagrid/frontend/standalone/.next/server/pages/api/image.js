"use strict";
(() => {
var exports = {};
exports.id = 941;
exports.ids = [941];
exports.modules = {

/***/ "(api)/./pages/api/image.js":
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

// ESM COMPAT FLAG
__webpack_require__.r(__webpack_exports__);

// EXPORTS
__webpack_require__.d(__webpack_exports__, {
  "default": () => (/* binding */ handler)
});

;// CONCATENATED MODULE: external "axios"
const external_axios_namespaceObject = require("axios");
var external_axios_default = /*#__PURE__*/__webpack_require__.n(external_axios_namespaceObject);
;// CONCATENATED MODULE: ./pages/api/image.js

async function handler(req, res) {
    const url = req?.query?.url;
    if (!url) {
        return res.status(400).json({
            message: "URL parameter not present in request body"
        });
    }
    const stream = await external_axios_default().request({
        url,
        responseType: "stream"
    });
    if (stream.status === 200) {
        await stream.data.pipe(res);
    } else {
        return res.status(stream.status);
    }
};


/***/ })

};
;

// load runtime
var __webpack_require__ = require("../../webpack-api-runtime.js");
__webpack_require__.C(exports);
var __webpack_exec__ = (moduleId) => (__webpack_require__(__webpack_require__.s = moduleId))
var __webpack_exports__ = (__webpack_exec__("(api)/./pages/api/image.js"));
module.exports = __webpack_exports__;

})();