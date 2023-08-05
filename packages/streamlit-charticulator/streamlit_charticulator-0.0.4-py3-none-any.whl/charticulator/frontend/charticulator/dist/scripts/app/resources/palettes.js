"use strict";
var __assign = (this && this.__assign) || function () {
    __assign = Object.assign || function(t) {
        for (var s, i = 1, n = arguments.length; i < n; i++) {
            s = arguments[i];
            for (var p in s) if (Object.prototype.hasOwnProperty.call(s, p))
                t[p] = s[p];
        }
        return t;
    };
    return __assign.apply(this, arguments);
};
var __read = (this && this.__read) || function (o, n) {
    var m = typeof Symbol === "function" && o[Symbol.iterator];
    if (!m) return o;
    var i = m.call(o), r, ar = [], e;
    try {
        while ((n === void 0 || n-- > 0) && !(r = i.next()).done) ar.push(r.value);
    }
    catch (error) { e = { error: error }; }
    finally {
        try {
            if (r && !r.done && (m = i["return"])) m.call(i);
        }
        finally { if (e) throw e.error; }
    }
    return ar;
};
Object.defineProperty(exports, "__esModule", { value: true });
exports.addColorPalette = exports.addPowerBIThemeColors = exports.transformPowerBIThemeColors = exports.addPalette = exports.predefinedPalettes = void 0;
// Copyright (c) Microsoft Corporation. All rights reserved.
// Licensed under the MIT license.
var core_1 = require("../../core");
exports.predefinedPalettes = [];
var converter = core_1.getColorConverter("sRGB", "sRGB");
function addPalette(name, type) {
    var colors = [];
    for (var _i = 2; _i < arguments.length; _i++) {
        colors[_i - 2] = arguments[_i];
    }
    exports.predefinedPalettes.push({
        name: name,
        type: type,
        colors: colors.map(function (x) {
            return x.map(function (y) {
                var c = core_1.colorFromHTMLColor(y);
                var _a = __read(converter(c.r, c.g, c.b), 3), r = _a[0], g = _a[1], b = _a[2];
                return { r: r, g: g, b: b };
            });
        }),
    });
}
exports.addPalette = addPalette;
function transformPowerBIThemeColors(colors) {
    var columnAmount = 10;
    var newColors = [];
    for (var i = 0; i < columnAmount; i++) {
        newColors.push([]);
    }
    for (var i = 0; i < colors.length; i++) {
        newColors[i % columnAmount].push(colors[i]);
    }
    return newColors;
}
exports.transformPowerBIThemeColors = transformPowerBIThemeColors;
function addPowerBIThemeColors() {
    var amount = 60;
    var colors = core_1.getDefaultColorPalette(amount);
    if (colors.length == amount) {
        var newColorArr = transformPowerBIThemeColors(colors);
        var colorPalette = {
            name: "Palette/Power BI Theme",
            type: "palette",
            colors: newColorArr,
        };
        addColorPalette(colorPalette);
        var resetFn = core_1.getDefaultColorGeneratorResetFunction();
        if (resetFn) {
            resetFn();
        }
    }
}
exports.addPowerBIThemeColors = addPowerBIThemeColors;
/* eslint-disable no-var */
//singleton
var flag = false;
function addColorPalette(colorPalette) {
    if (!flag) {
        exports.predefinedPalettes.push(__assign({}, colorPalette));
        flag = true;
    }
}
exports.addColorPalette = addColorPalette;
// D3 colors
addPalette("D3/Category 10", "qualitative", [
    "#1f77b4",
    "#ff7f0e",
    "#2ca02c",
    "#d62728",
    "#9467bd",
    "#8c564b",
    "#e377c2",
    "#7f7f7f",
    "#bcbd22",
    "#17becf",
]);
addPalette("D3/Category 20", "qualitative", [
    "#1f77b4",
    "#aec7e8",
    "#ff7f0e",
    "#ffbb78",
    "#2ca02c",
    "#98df8a",
    "#d62728",
    "#ff9896",
    "#9467bd",
    "#c5b0d5",
    "#8c564b",
    "#c49c94",
    "#e377c2",
    "#f7b6d2",
    "#7f7f7f",
    "#c7c7c7",
    "#bcbd22",
    "#dbdb8d",
    "#17becf",
    "#9edae5",
]);
addPalette("D3/Category 20 b", "qualitative", [
    "#393b79",
    "#5254a3",
    "#6b6ecf",
    "#9c9ede",
    "#637939",
    "#8ca252",
    "#b5cf6b",
    "#cedb9c",
    "#8c6d31",
    "#bd9e39",
    "#e7ba52",
    "#e7cb94",
    "#843c39",
    "#ad494a",
    "#d6616b",
    "#e7969c",
    "#7b4173",
    "#a55194",
    "#ce6dbd",
    "#de9ed6",
]);
addPalette("D3/Category 20 c", "qualitative", [
    "#3182bd",
    "#6baed6",
    "#9ecae1",
    "#c6dbef",
    "#e6550d",
    "#fd8d3c",
    "#fdae6b",
    "#fdd0a2",
    "#31a354",
    "#74c476",
    "#a1d99b",
    "#c7e9c0",
    "#756bb1",
    "#9e9ac8",
    "#bcbddc",
    "#dadaeb",
    "#636363",
    "#969696",
    "#bdbdbd",
    "#d9d9d9",
]);
addPalette("Palette/ColorBrewer", "palette", [
    "#fff5f0",
    "#fee0d2",
    "#fcbba1",
    "#fc9272",
    "#fb6a4a",
    "#ef3b2c",
    "#cb181d",
    "#a50f15",
    "#67000d",
].reverse(), [
    "#fff5eb",
    "#fee6ce",
    "#fdd0a2",
    "#fdae6b",
    "#fd8d3c",
    "#f16913",
    "#d94801",
    "#a63603",
    "#7f2704",
].reverse(), [
    "#f7fcf5",
    "#e5f5e0",
    "#c7e9c0",
    "#a1d99b",
    "#74c476",
    "#41ab5d",
    "#238b45",
    "#006d2c",
    "#00441b",
].reverse(), [
    "#f7fbff",
    "#deebf7",
    "#c6dbef",
    "#9ecae1",
    "#6baed6",
    "#4292c6",
    "#2171b5",
    "#08519c",
    "#08306b",
].reverse(), [
    "#fcfbfd",
    "#efedf5",
    "#dadaeb",
    "#bcbddc",
    "#9e9ac8",
    "#807dba",
    "#6a51a3",
    "#54278f",
    "#3f007d",
].reverse(), [
    "#ffffff",
    "#f0f0f0",
    "#d9d9d9",
    "#bdbdbd",
    "#969696",
    "#737373",
    "#525252",
    "#252525",
    "#000000",
].reverse());
addPalette("Palette/Material", "palette", [
    "#fafafa",
    "#f5f5f5",
    "#eeeeee",
    "#e0e0e0",
    "#bdbdbd",
    "#9e9e9e",
    "#757575",
    "#616161",
    "#424242",
    "#212121",
].reverse(), [
    "#eceff1",
    "#cfd8dc",
    "#b0bec5",
    "#90a4ae",
    "#78909c",
    "#607d8b",
    "#546e7a",
    "#455a64",
    "#37474f",
    "#263238",
].reverse(), [
    "#efebe9",
    "#d7ccc8",
    "#bcaaa4",
    "#a1887f",
    "#8d6e63",
    "#795548",
    "#6d4c41",
    "#5d4037",
    "#4e342e",
    "#3e2723",
].reverse(), [
    "#ffebee",
    "#ffcdd2",
    "#ef9a9a",
    "#e57373",
    "#ef5350",
    "#f44336",
    "#e53935",
    "#d32f2f",
    "#c62828",
    "#b71c1c",
].reverse(), [
    "#fce4ec",
    "#f8bbd0",
    "#f48fb1",
    "#f06292",
    "#ec407a",
    "#e91e63",
    "#d81b60",
    "#c2185b",
    "#ad1457",
    "#880e4f",
].reverse(), [
    "#f3e5f5",
    "#e1bee7",
    "#ce93d8",
    "#ba68c8",
    "#ab47bc",
    "#9c27b0",
    "#8e24aa",
    "#7b1fa2",
    "#6a1b9a",
    "#4a148c",
].reverse(), [
    "#ede7f6",
    "#d1c4e9",
    "#b39ddb",
    "#9575cd",
    "#7e57c2",
    "#673ab7",
    "#5e35b1",
    "#512da8",
    "#4527a0",
    "#311b92",
].reverse(), [
    "#e8eaf6",
    "#c5cae9",
    "#9fa8da",
    "#7986cb",
    "#5c6bc0",
    "#3f51b5",
    "#3949ab",
    "#303f9f",
    "#283593",
    "#1a237e",
].reverse(), [
    "#e3f2fd",
    "#bbdefb",
    "#90caf9",
    "#64b5f6",
    "#42a5f5",
    "#2196f3",
    "#1e88e5",
    "#1976d2",
    "#1565c0",
    "#0d47a1",
].reverse(), [
    "#e1f5fe",
    "#b3e5fc",
    "#81d4fa",
    "#4fc3f7",
    "#29b6f6",
    "#03a9f4",
    "#039be5",
    "#0288d1",
    "#0277bd",
    "#01579b",
].reverse(), [
    "#e0f7fa",
    "#b2ebf2",
    "#80deea",
    "#4dd0e1",
    "#26c6da",
    "#00bcd4",
    "#00acc1",
    "#0097a7",
    "#00838f",
    "#006064",
].reverse(), [
    "#e0f2f1",
    "#b2dfdb",
    "#80cbc4",
    "#4db6ac",
    "#26a69a",
    "#009688",
    "#00897b",
    "#00796b",
    "#00695c",
    "#004d40",
].reverse(), [
    "#e8f5e9",
    "#c8e6c9",
    "#a5d6a7",
    "#81c784",
    "#66bb6a",
    "#4caf50",
    "#43a047",
    "#388e3c",
    "#2e7d32",
    "#1b5e20",
].reverse(), [
    "#f1f8e9",
    "#dcedc8",
    "#c5e1a5",
    "#aed581",
    "#9ccc65",
    "#8bc34a",
    "#7cb342",
    "#689f38",
    "#558b2f",
    "#33691e",
].reverse(), [
    "#f9fbe7",
    "#f0f4c3",
    "#e6ee9c",
    "#dce775",
    "#d4e157",
    "#cddc39",
    "#c0ca33",
    "#afb42b",
    "#9e9d24",
    "#827717",
].reverse(), [
    "#fffde7",
    "#fff9c4",
    "#fff59d",
    "#fff176",
    "#ffee58",
    "#ffeb3b",
    "#fdd835",
    "#fbc02d",
    "#f9a825",
    "#f57f17",
].reverse(), [
    "#fff8e1",
    "#ffecb3",
    "#ffe082",
    "#ffd54f",
    "#ffca28",
    "#ffc107",
    "#ffb300",
    "#ffa000",
    "#ff8f00",
    "#ff6f00",
].reverse(), [
    "#fff3e0",
    "#ffe0b2",
    "#ffcc80",
    "#ffb74d",
    "#ffa726",
    "#ff9800",
    "#fb8c00",
    "#f57c00",
    "#ef6c00",
    "#e65100",
].reverse(), [
    "#fbe9e7",
    "#ffccbc",
    "#ffab91",
    "#ff8a65",
    "#ff7043",
    "#ff5722",
    "#f4511e",
    "#e64a19",
    "#d84315",
    "#bf360c",
].reverse());
addPalette("Palette/Universal", "palette", [
    "#f2f2f2",
    "#e6e6e6",
    "#cccccc",
    "#767676",
    "#393939",
    "#2b2b2b",
    "#1f1f1f",
].reverse(), [
    "#cbc6c4",
    "#b1adab",
    "#989391",
    "#7a7574",
    "#6e6a68",
    "#5d5a58",
    "#4c4a48",
].reverse(), [
    "#bac8cc",
    "#a0aeb2",
    "#859599",
    "#69797e",
    "#5a686c",
    "#4a5459",
    "#394146",
].reverse(), [
    "#cae0d9",
    "#a3bfb7",
    "#7d9d95",
    "#567c73",
    "#486860",
    "#3b534d",
    "#2d3f3a",
].reverse(), [
    "#f7d7c4",
    "#d8b094",
    "#bb9167",
    "#ac744c",
    "#8e562e",
    "#603d30",
    "#4d291c",
].reverse(), [
    "#ffc0c0",
    "#ff8c8c",
    "#ff6767",
    "#ff4343",
    "#d13438",
    "#a4262c",
    "#761721",
].reverse(), [
    "#f4abba",
    "#e6808a",
    "#e74856",
    "#e81123",
    "#c50f1f",
    "#a80000",
    "#750b1c",
].reverse(), [
    "#edbed3",
    "#ed7eac",
    "#ee3f86",
    "#ea005e",
    "#c30052",
    "#970044",
    "#6b0036",
].reverse(), [
    "#e8a3de",
    "#e66fc2",
    "#e43ba6",
    "#e3008c",
    "#bf0077",
    "#9b0062",
    "#77004d",
].reverse(), [
    "#de94e0",
    "#d066c9",
    "#c239b3",
    "#b4009e",
    "#9a0089",
    "#800074",
    "#5c005c",
].reverse(), [
    "#dea2ed",
    "#c774d7",
    "#b146c2",
    "#881798",
    "#721481",
    "#5c126b",
    "#460f54",
].reverse(), [
    "#cfc4f5",
    "#ab94d6",
    "#8764b8",
    "#744da9",
    "#5c2e91",
    "#4e257f",
    "#401b6c",
].reverse(), [
    "#c3c3f4",
    "#afa6ee",
    "#9c89e9",
    "#886ce4",
    "#735bc1",
    "#5e4a9d",
    "#49397a",
].reverse(), [
    "#b5b5e2",
    "#9c96e0",
    "#8378de",
    "#7160e8",
    "#5a4ebc",
    "#49409a",
    "#373277",
].reverse(), [
    "#bebee5",
    "#9493dd",
    "#6b69d6",
    "#4f4bd9",
    "#413eb3",
    "#32318c",
    "#242466",
].reverse(), [
    "#a6bdff",
    "#7c96f9",
    "#4f6bed",
    "#2849ec",
    "#203dbd",
    "#19318d",
    "#11255e",
].reverse(), [
    "#abc9ed",
    "#7ba7ff",
    "#3b78ff",
    "#0046ff",
    "#0037da",
    "#0027b4",
    "#00188f",
].reverse(), [
    "#b3dbf2",
    "#83beec",
    "#3a96dd",
    "#0078d7",
    "#0063b1",
    "#004e8c",
    "#003966",
].reverse(), [
    "#99ecff",
    "#69eaff",
    "#31d2f7",
    "#00bcf2",
    "#0099bc",
    "#006f94",
    "#005b70",
].reverse(), [
    "#91e5df",
    "#61d6d6",
    "#30c6cc",
    "#00b7c3",
    "#009ca4",
    "#038387",
    "#006666",
].reverse(), [
    "#c2f2e9",
    "#81e6d3",
    "#41dabc",
    "#00cea6",
    "#00b294",
    "#008272",
    "#005e50",
].reverse(), [
    "#a8e5c2",
    "#70dda5",
    "#38d487",
    "#00cc6a",
    "#00ae56",
    "#10893e",
    "#00722e",
].reverse(), [
    "#aae5aa",
    "#79db75",
    "#47d041",
    "#16c60c",
    "#13a10e",
    "#107c10",
    "#0b6a0b",
].reverse(), [
    "#d5e5ae",
    "#b7df74",
    "#9ad93a",
    "#7cd300",
    "#6bb700",
    "#599b00",
    "#498205",
].reverse(), [
    "#f8ffb3",
    "#e4f577",
    "#d1ec3c",
    "#bad80a",
    "#a4cf0c",
    "#8cbd18",
    "#73aa24",
].reverse(), [
    "#f9f1a5",
    "#faec6e",
    "#fff100",
    "#fce100",
    "#dfbe00",
    "#c19c00",
    "#986f0b",
].reverse(), [
    "#ffe5b6",
    "#ffd679",
    "#ffc83d",
    "#ffb900",
    "#eaa300",
    "#d48c00",
    "#ab620d",
].reverse(), [
    "#ffdabb",
    "#ffc988",
    "#ffaa44",
    "#ff8c00",
    "#d47300",
    "#b05e0d",
    "#7f4200",
].reverse(), [
    "#f2d5c9",
    "#f7b189",
    "#f7894a",
    "#f7630c",
    "#ca5010",
    "#a74109",
    "#7f2f08",
].reverse(), [
    "#eec7c2",
    "#ee9889",
    "#ef6950",
    "#f03a17",
    "#da3b01",
    "#a52613",
    "#7f1d10",
].reverse());
addPalette("Palette/Power BI", "palette", ["#666666", "#808080", "#b3b3b3", "#cccccc", "#e6e6e6", "#ffffff"].reverse(), ["#000000", "#1a1a1a", "#333333", "#666666", "#999999", "#000000"].reverse(), ["#015c55", "#018a80", "#34c6bb", "#67d4cc", "#99e3dd", "#01b8aa"].reverse(), ["#1c2325", "#293537", "#5f6b6d", "#879092", "#afb5b6", "#374649"].reverse(), ["#7f312f", "#be4a47", "#fd817e", "#fea19e", "#fec0bf", "#fd625e"].reverse(), ["#796408", "#b6960b", "#f5d33f", "#f7de6f", "#fae99f", "#f2c80f"].reverse(), ["#303637", "#475052", "#7f898a", "#9fa6a7", "#bfc4c5", "#5f6b6d"].reverse(), ["#456a76", "#689fb0", "#a1ddef", "#b9e5f3", "#d0eef7", "#8ad4eb"].reverse(), ["#118dff", "#a0d1ff", "#70bbff", "#41a4ff", "#0d6abf", "#094780"].reverse(), ["#7f4b33", "#bf714d", "#feab85", "#fec0a3", "#ffd5c2", "#fe9666"].reverse(), ["#53354d", "#7d4f73", "#b887ad", "#caa5c2", "#dbc3d6", "#a66999"].reverse());
// Single hue
addPalette("ColorBrewer/Reds", "sequential", [
    "#fff5f0",
    "#fee0d2",
    "#fcbba1",
    "#fc9272",
    "#fb6a4a",
    "#ef3b2c",
    "#cb181d",
    "#a50f15",
    "#67000d",
]);
addPalette("ColorBrewer/Oranges", "sequential", [
    "#fff5eb",
    "#fee6ce",
    "#fdd0a2",
    "#fdae6b",
    "#fd8d3c",
    "#f16913",
    "#d94801",
    "#a63603",
    "#7f2704",
]);
addPalette("ColorBrewer/Greens", "sequential", [
    "#f7fcf5",
    "#e5f5e0",
    "#c7e9c0",
    "#a1d99b",
    "#74c476",
    "#41ab5d",
    "#238b45",
    "#006d2c",
    "#00441b",
]);
addPalette("ColorBrewer/Blues", "sequential", [
    "#f7fbff",
    "#deebf7",
    "#c6dbef",
    "#9ecae1",
    "#6baed6",
    "#4292c6",
    "#2171b5",
    "#08519c",
    "#08306b",
]);
addPalette("ColorBrewer/Purples", "sequential", [
    "#fcfbfd",
    "#efedf5",
    "#dadaeb",
    "#bcbddc",
    "#9e9ac8",
    "#807dba",
    "#6a51a3",
    "#54278f",
    "#3f007d",
]);
addPalette("ColorBrewer/Greys", "sequential", [
    "#ffffff",
    "#f0f0f0",
    "#d9d9d9",
    "#bdbdbd",
    "#969696",
    "#737373",
    "#525252",
    "#252525",
    "#000000",
]);
// Diverging
addPalette("ColorBrewer/BrBG", "diverging", [
    "#543005",
    "#8c510a",
    "#bf812d",
    "#dfc27d",
    "#f6e8c3",
    "#f5f5f5",
    "#c7eae5",
    "#80cdc1",
    "#35978f",
    "#01665e",
    "#003c30",
].reverse());
addPalette("ColorBrewer/PiYG", "diverging", [
    "#8e0152",
    "#c51b7d",
    "#de77ae",
    "#f1b6da",
    "#fde0ef",
    "#f7f7f7",
    "#e6f5d0",
    "#b8e186",
    "#7fbc41",
    "#4d9221",
    "#276419",
].reverse());
addPalette("ColorBrewer/PRGn", "diverging", [
    "#40004b",
    "#762a83",
    "#9970ab",
    "#c2a5cf",
    "#e7d4e8",
    "#f7f7f7",
    "#d9f0d3",
    "#a6dba0",
    "#5aae61",
    "#1b7837",
    "#00441b",
].reverse());
addPalette("ColorBrewer/PuOr", "diverging", [
    "#7f3b08",
    "#b35806",
    "#e08214",
    "#fdb863",
    "#fee0b6",
    "#f7f7f7",
    "#d8daeb",
    "#b2abd2",
    "#8073ac",
    "#542788",
    "#2d004b",
].reverse());
addPalette("ColorBrewer/RdBu", "diverging", [
    "#67001f",
    "#b2182b",
    "#d6604d",
    "#f4a582",
    "#fddbc7",
    "#f7f7f7",
    "#d1e5f0",
    "#92c5de",
    "#4393c3",
    "#2166ac",
    "#053061",
].reverse());
addPalette("ColorBrewer/RdGy", "diverging", [
    "#67001f",
    "#b2182b",
    "#d6604d",
    "#f4a582",
    "#fddbc7",
    "#ffffff",
    "#e0e0e0",
    "#bababa",
    "#878787",
    "#4d4d4d",
    "#1a1a1a",
].reverse());
addPalette("ColorBrewer/RdYlBu", "diverging", [
    "#a50026",
    "#d73027",
    "#f46d43",
    "#fdae61",
    "#fee090",
    "#ffffbf",
    "#e0f3f8",
    "#abd9e9",
    "#74add1",
    "#4575b4",
    "#313695",
].reverse());
addPalette("ColorBrewer/RdYlGn", "diverging", [
    "#a50026",
    "#d73027",
    "#f46d43",
    "#fdae61",
    "#fee08b",
    "#ffffbf",
    "#d9ef8b",
    "#a6d96a",
    "#66bd63",
    "#1a9850",
    "#006837",
].reverse());
addPalette("ColorBrewer/Spectral", "diverging", [
    "#9e0142",
    "#d53e4f",
    "#f46d43",
    "#fdae61",
    "#fee08b",
    "#ffffbf",
    "#e6f598",
    "#abdda4",
    "#66c2a5",
    "#3288bd",
    "#5e4fa2",
].reverse());
addPalette("ColorBrewer/BuGn", "sequential", [
    "#f7fcfd",
    "#e5f5f9",
    "#ccece6",
    "#99d8c9",
    "#66c2a4",
    "#41ae76",
    "#238b45",
    "#006d2c",
    "#00441b",
]);
addPalette("ColorBrewer/BuPu", "sequential", [
    "#f7fcfd",
    "#e0ecf4",
    "#bfd3e6",
    "#9ebcda",
    "#8c96c6",
    "#8c6bb1",
    "#88419d",
    "#810f7c",
    "#4d004b",
]);
addPalette("ColorBrewer/GnBu", "sequential", [
    "#f7fcf0",
    "#e0f3db",
    "#ccebc5",
    "#a8ddb5",
    "#7bccc4",
    "#4eb3d3",
    "#2b8cbe",
    "#0868ac",
    "#084081",
]);
addPalette("ColorBrewer/OrRd", "sequential", [
    "#fff7ec",
    "#fee8c8",
    "#fdd49e",
    "#fdbb84",
    "#fc8d59",
    "#ef6548",
    "#d7301f",
    "#b30000",
    "#7f0000",
]);
addPalette("ColorBrewer/PuBu", "sequential", [
    "#fff7fb",
    "#ece7f2",
    "#d0d1e6",
    "#a6bddb",
    "#74a9cf",
    "#3690c0",
    "#0570b0",
    "#045a8d",
    "#023858",
]);
addPalette("ColorBrewer/PuBuGn", "sequential", [
    "#fff7fb",
    "#ece2f0",
    "#d0d1e6",
    "#a6bddb",
    "#67a9cf",
    "#3690c0",
    "#02818a",
    "#016c59",
    "#014636",
]);
addPalette("ColorBrewer/PuRd", "sequential", [
    "#f7f4f9",
    "#e7e1ef",
    "#d4b9da",
    "#c994c7",
    "#df65b0",
    "#e7298a",
    "#ce1256",
    "#980043",
    "#67001f",
]);
addPalette("ColorBrewer/RdPu", "sequential", [
    "#fff7f3",
    "#fde0dd",
    "#fcc5c0",
    "#fa9fb5",
    "#f768a1",
    "#dd3497",
    "#ae017e",
    "#7a0177",
    "#49006a",
]);
addPalette("ColorBrewer/YlGn", "sequential", [
    "#ffffe5",
    "#f7fcb9",
    "#d9f0a3",
    "#addd8e",
    "#78c679",
    "#41ab5d",
    "#238443",
    "#006837",
    "#004529",
]);
addPalette("ColorBrewer/YlGnBu", "sequential", [
    "#ffffd9",
    "#edf8b1",
    "#c7e9b4",
    "#7fcdbb",
    "#41b6c4",
    "#1d91c0",
    "#225ea8",
    "#253494",
    "#081d58",
]);
addPalette("ColorBrewer/YlOrBr", "sequential", [
    "#ffffe5",
    "#fff7bc",
    "#fee391",
    "#fec44f",
    "#fe9929",
    "#ec7014",
    "#cc4c02",
    "#993404",
    "#662506",
]);
addPalette("ColorBrewer/YlOrRd", "sequential", [
    "#ffffcc",
    "#ffeda0",
    "#fed976",
    "#feb24c",
    "#fd8d3c",
    "#fc4e2a",
    "#e31a1c",
    "#bd0026",
    "#800026",
]);
// Qualitative
addPalette("ColorBrewer/Accent", "qualitative", [
    "#7fc97f",
    "#beaed4",
    "#fdc086",
    "#ffff99",
    "#386cb0",
    "#f0027f",
    "#bf5b17",
    "#666666",
]);
addPalette("ColorBrewer/Dark2", "qualitative", [
    "#1b9e77",
    "#d95f02",
    "#7570b3",
    "#e7298a",
    "#66a61e",
    "#e6ab02",
    "#a6761d",
    "#666666",
]);
addPalette("ColorBrewer/Paired", "qualitative", [
    "#a6cee3",
    "#1f78b4",
    "#b2df8a",
    "#33a02c",
    "#fb9a99",
    "#e31a1c",
    "#fdbf6f",
    "#ff7f00",
    "#cab2d6",
    "#6a3d9a",
    "#ffff99",
    "#b15928",
]);
addPalette("ColorBrewer/Pastel1", "qualitative", [
    "#fbb4ae",
    "#b3cde3",
    "#ccebc5",
    "#decbe4",
    "#fed9a6",
    "#ffffcc",
    "#e5d8bd",
    "#fddaec",
    "#f2f2f2",
]);
addPalette("ColorBrewer/Pastel2", "qualitative", [
    "#b3e2cd",
    "#fdcdac",
    "#cbd5e8",
    "#f4cae4",
    "#e6f5c9",
    "#fff2ae",
    "#f1e2cc",
    "#cccccc",
]);
addPalette("ColorBrewer/Set1", "qualitative", [
    "#e41a1c",
    "#377eb8",
    "#4daf4a",
    "#984ea3",
    "#ff7f00",
    "#ffff33",
    "#a65628",
    "#f781bf",
    "#999999",
]);
addPalette("ColorBrewer/Set2", "qualitative", [
    "#66c2a5",
    "#fc8d62",
    "#8da0cb",
    "#e78ac3",
    "#a6d854",
    "#ffd92f",
    "#e5c494",
    "#b3b3b3",
]);
addPalette("ColorBrewer/Set3", "qualitative", [
    "#8dd3c7",
    "#ffffb3",
    "#bebada",
    "#fb8072",
    "#80b1d3",
    "#fdb462",
    "#b3de69",
    "#fccde5",
    "#d9d9d9",
    "#bc80bd",
    "#ccebc5",
    "#ffed6f",
]);
//# sourceMappingURL=palettes.js.map