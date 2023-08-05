"use strict";
var __extends = (this && this.__extends) || (function () {
    var extendStatics = function (d, b) {
        extendStatics = Object.setPrototypeOf ||
            ({ __proto__: [] } instanceof Array && function (d, b) { d.__proto__ = b; }) ||
            function (d, b) { for (var p in b) if (b.hasOwnProperty(p)) d[p] = b[p]; };
        return extendStatics(d, b);
    };
    return function (d, b) {
        extendStatics(d, b);
        function __() { this.constructor = d; }
        d.prototype = b === null ? Object.create(b) : (__.prototype = b.prototype, new __());
    };
})();
Object.defineProperty(exports, "__esModule", { value: true });
exports.HorizontalSplitPaneView = void 0;
// Copyright (c) Microsoft Corporation. All rights reserved.
// Licensed under the MIT license.
var React = require("react");
var HorizontalSplitPaneView = /** @class */ (function (_super) {
    __extends(HorizontalSplitPaneView, _super);
    function HorizontalSplitPaneView() {
        return _super !== null && _super.apply(this, arguments) || this;
    }
    HorizontalSplitPaneView.prototype.render = function () {
        return (React.createElement("div", { className: "split-pane-view-horizontal" },
            React.createElement("div", { className: "row" }, React.Children.map(this.props.children, function (child) { return (React.createElement("div", { className: "pane" }, child)); }))));
    };
    return HorizontalSplitPaneView;
}(React.Component));
exports.HorizontalSplitPaneView = HorizontalSplitPaneView;
//# sourceMappingURL=split_panes.js.map