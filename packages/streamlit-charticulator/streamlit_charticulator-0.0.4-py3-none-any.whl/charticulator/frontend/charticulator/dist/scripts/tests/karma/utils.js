"use strict";
var __awaiter = (this && this.__awaiter) || function (thisArg, _arguments, P, generator) {
    function adopt(value) { return value instanceof P ? value : new P(function (resolve) { resolve(value); }); }
    return new (P || (P = Promise))(function (resolve, reject) {
        function fulfilled(value) { try { step(generator.next(value)); } catch (e) { reject(e); } }
        function rejected(value) { try { step(generator["throw"](value)); } catch (e) { reject(e); } }
        function step(result) { result.done ? resolve(result.value) : adopt(result.value).then(fulfilled, rejected); }
        step((generator = generator.apply(thisArg, _arguments || [])).next());
    });
};
var __generator = (this && this.__generator) || function (thisArg, body) {
    var _ = { label: 0, sent: function() { if (t[0] & 1) throw t[1]; return t[1]; }, trys: [], ops: [] }, f, y, t, g;
    return g = { next: verb(0), "throw": verb(1), "return": verb(2) }, typeof Symbol === "function" && (g[Symbol.iterator] = function() { return this; }), g;
    function verb(n) { return function (v) { return step([n, v]); }; }
    function step(op) {
        if (f) throw new TypeError("Generator is already executing.");
        while (_) try {
            if (f = 1, y && (t = op[0] & 2 ? y["return"] : op[0] ? y["throw"] || ((t = y["return"]) && t.call(y), 0) : y.next) && !(t = t.call(y, op[1])).done) return t;
            if (y = 0, t) op = [op[0] & 2, t.value];
            switch (op[0]) {
                case 0: case 1: t = op; break;
                case 4: _.label++; return { value: op[1], done: false };
                case 5: _.label++; y = op[1]; op = [0]; continue;
                case 7: op = _.ops.pop(); _.trys.pop(); continue;
                default:
                    if (!(t = _.trys, t = t.length > 0 && t[t.length - 1]) && (op[0] === 6 || op[0] === 2)) { _ = 0; continue; }
                    if (op[0] === 3 && (!t || (op[1] > t[0] && op[1] < t[3]))) { _.label = op[1]; break; }
                    if (op[0] === 6 && _.label < t[1]) { _.label = t[1]; t = op; break; }
                    if (t && _.label < t[2]) { _.label = t[2]; _.ops.push(op); break; }
                    if (t[2]) _.ops.pop();
                    _.trys.pop(); continue;
            }
            op = body.call(thisArg, _);
        } catch (e) { op = [6, e]; y = 0; } finally { f = t = 0; }
        if (op[0] & 5) throw op[1]; return { value: op[0] ? op[1] : void 0, done: true };
    }
};
var __values = (this && this.__values) || function(o) {
    var s = typeof Symbol === "function" && Symbol.iterator, m = s && o[s], i = 0;
    if (m) return m.call(o);
    if (o && typeof o.length === "number") return {
        next: function () {
            if (o && i >= o.length) o = void 0;
            return { value: o && o[i++], done: !o };
        }
    };
    throw new TypeError(s ? "Object is not iterable." : "Symbol.iterator is not defined.");
};
Object.defineProperty(exports, "__esModule", { value: true });
exports.pathPrefix = exports.shortTimeOut = exports.mediumTimeOut = exports.longTimeOut = exports.getLinkTypePanel = exports.clickOnButtonByTitle = exports.clickOnToolbarButton = exports.findElementsByClassID = exports.getChartCanvas = exports.closeStartMenuPanel = void 0;
// Copyright (c) Microsoft Corporation. All rights reserved.
// Licensed under the MIT license.
var core_1 = require("../../core");
function closeStartMenuPanel() {
    document
        .querySelector(".popup-container-modal .el-button-back")
        .click();
}
exports.closeStartMenuPanel = closeStartMenuPanel;
function getChartCanvas() {
    return document.querySelector("div.chart-editor-canvas-view > svg.canvas-view");
}
exports.getChartCanvas = getChartCanvas;
function findElementsByClassID(chart, classID) {
    var _a, _b, item, e_1_1;
    var e_1, _c;
    return __generator(this, function (_d) {
        switch (_d.label) {
            case 0:
                _d.trys.push([0, 5, 6, 7]);
                _a = __values(core_1.Prototypes.forEachObject(chart)), _b = _a.next();
                _d.label = 1;
            case 1:
                if (!!_b.done) return [3 /*break*/, 4];
                item = _b.value;
                if (!core_1.Prototypes.isType(item.object.classID, classID)) return [3 /*break*/, 3];
                return [4 /*yield*/, item];
            case 2:
                _d.sent();
                _d.label = 3;
            case 3:
                _b = _a.next();
                return [3 /*break*/, 1];
            case 4: return [3 /*break*/, 7];
            case 5:
                e_1_1 = _d.sent();
                e_1 = { error: e_1_1 };
                return [3 /*break*/, 7];
            case 6:
                try {
                    if (_b && !_b.done && (_c = _a.return)) _c.call(_a);
                }
                finally { if (e_1) throw e_1.error; }
                return [7 /*endfinally*/];
            case 7: return [2 /*return*/];
        }
    });
}
exports.findElementsByClassID = findElementsByClassID;
function clickOnToolbarButton(buttonName) {
    return __awaiter(this, void 0, void 0, function () {
        return __generator(this, function (_a) {
            document
                .querySelector("button[title=\"" + buttonName + "\"]")
                .click();
            return [2 /*return*/, new Promise(function (resolve) {
                    setTimeout(resolve, 100);
                })];
        });
    });
}
exports.clickOnToolbarButton = clickOnToolbarButton;
function clickOnButtonByTitle(buttonName) {
    return __awaiter(this, void 0, void 0, function () {
        return __generator(this, function (_a) {
            document
                .querySelector("button[title=\"" + buttonName + "\"]")
                .click();
            return [2 /*return*/, new Promise(function (resolve) {
                    setTimeout(resolve, 100);
                })];
        });
    });
}
exports.clickOnButtonByTitle = clickOnButtonByTitle;
function getLinkTypePanel() {
    return document.querySelector("div.charticulator__link-type-table");
}
exports.getLinkTypePanel = getLinkTypePanel;
exports.longTimeOut = 1000000;
exports.mediumTimeOut = 100000;
exports.shortTimeOut = 3000;
// The directory containing chart cases
exports.pathPrefix = "tests/unit/charts";
//# sourceMappingURL=utils.js.map