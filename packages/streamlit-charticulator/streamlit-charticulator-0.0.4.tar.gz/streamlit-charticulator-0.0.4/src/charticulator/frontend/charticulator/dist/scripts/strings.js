"use strict";
// Copyright (c) Microsoft Corporation. All rights reserved.
// Licensed under the MIT license.
Object.defineProperty(exports, "__esModule", { value: true });
exports.strings = void 0;
var cartesianTerminology = {
    xAxis: "X Axis",
    yAxis: "Y Axis",
    xMin: "Left",
    xMiddle: "Middle",
    xMax: "Right",
    yMiddle: "Middle",
    yMin: "Bottom",
    yMax: "Top",
    dodgeX: "Stack X",
    dodgeY: "Stack Y",
    grid: "Grid",
    gridDirectionX: "Horizontal",
    gridDirectionY: "Vertical",
    packing: "Packing",
    jitter: "Jitter",
    overlap: "Overlap",
};
var curveTerminology = {
    xAxis: "Tangent Axis",
    yAxis: "Normal Axis",
    xMin: "Left",
    xMiddle: "Middle",
    xMax: "Right",
    yMiddle: "Middle",
    yMin: "Bottom",
    yMax: "Top",
    dodgeX: "Stack Tangential",
    dodgeY: "Stack Normal",
    grid: "Grid",
    gridDirectionX: "Tangent",
    gridDirectionY: "Normal",
    packing: "Packing",
    jitter: "Jitter",
    overlap: "Overlap",
};
var polarTerminology = {
    xAxis: "Angular Axis",
    yAxis: "Radial Axis",
    xMin: "Left",
    xMiddle: "Middle",
    xMax: "Right",
    yMiddle: "Middle",
    yMin: "Bottom",
    yMax: "Top",
    dodgeX: "Stack Angular",
    dodgeY: "Stack Radial",
    grid: "Grid",
    gridDirectionX: "Angular",
    gridDirectionY: "Radial",
    packing: "Packing",
    jitter: "Jitter",
    overlap: "Overlap",
};
exports.strings = {
    app: {
        loading: "Loading...",
        name: "Microsoft Charticulator",
        nestedChartTitle: "Nested Chart | Charticulator",
        working: "Working...",
    },
    dialogs: {
        saveChanges: {
            saveChangesTitle: "Save the changes",
            saveChanges: function (chartName) {
                return "Do you want to save the changes you made to " + chartName + "?";
            },
        },
    },
    about: {
        version: function (version, url) {
            return "Version: " + version + ", URL: " + url;
        },
        license: "Show License",
    },
    button: {
        cancel: "Cancel",
        no: "No",
        yes: "Yes",
    },
    canvas: {
        markContainer: "To edit this glyph, please create a plot segment with it.",
        newGlyph: "New glyph",
        zoomAuto: "Auto zoom",
        zoomIn: "Zoom in",
        zoomOut: "Zoom out",
        sublayoutType: "Sublayout type",
        elementOrders: "Order of elements",
        gridDirection: "Grid row direction",
        alignItemsOnX: "Align items on X axis",
        alignItemsOnY: "Align items on Y axis",
    },
    dataset: {
        dimensions: function (rows, columns) {
            return rows + " rows, " + columns + " columns";
        },
        months: [
            "Jan",
            "Feb",
            "Mar",
            "Apr",
            "May",
            "Jun",
            "Jul",
            "Aug",
            "Sep",
            "Oct",
            "Nov",
            "Dec",
        ],
        replaceWithCSV: "Replace data with CSV file",
        showDataValues: "Show data values",
        showDerivedFields: "Show derived fields",
        tableTitleColumns: "Fields",
        tableTitleLinks: "Links",
        tableTitleImages: "Images",
        weekday: ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"],
    },
    defaultDataset: {
        city: "City",
        month: "Month",
        temperature: "Temperature",
        value: "Value",
    },
    dialog: {
        resetConfirm: "Are you sure you want to delete the chart?",
        deleteChart: "Delete chart",
    },
    scaleEditor: {
        add: "Add",
        removeLast: "Remove the last",
        addLegend: "Add Legend",
        removeLegend: "Remove Legend",
        removeSelected: "Remove",
        reverse: "Reverse",
    },
    legendCreator: {
        legendType: "Legend type:",
        connectBy: "Connect by:",
        createLegend: "Create Legend",
    },
    mappingEditor: {
        bindData: "Bind data",
        keyColumnExpression: "Key column expression",
        bindDataValue: "Bind data value",
        remove: "Remove",
        chooseColor: "Choose color",
    },
    error: {
        imageLoad: function (url) { return "failed to retrieve map image at url " + url; },
        notImplemented: "Not implemented yet",
        storeNotFound: function (componentName) {
            return "store not found in component " + componentName;
        },
    },
    fileExport: {
        asHTML: "Export as HTML",
        asImage: "Export as Image",
        inferAxisMin: function (objectName, inferenceAxisProperty) {
            return "Auto min values for " + objectName + "/" + inferenceAxisProperty;
        },
        inferAxisMax: function (objectName, inferenceAxisProperty) {
            return "Auto max values for " + objectName + "/" + inferenceAxisProperty;
        },
        inferScaleMin: function (objectName) { return "Auto min domain for " + objectName; },
        inferScaleMax: function (objectName) { return "Auto max domain for " + objectName; },
        imageDPI: "DPI (for PNG/JPEG)",
        labelAxesAndScales: "Axes and Scales",
        labelExposedObjects: "Exposed Objects",
        labelProperties: function (exportKind) { return exportKind + " Properties"; },
        labelSlots: "Data Mapping Slots",
        slotColumnExample: function (columnName) { return columnName + " examples"; },
        slotColumnName: function (columnName) { return columnName + " name"; },
        typeHTML: "HTML",
        typeJPEG: "JPEG",
        typePNG: "PNG",
        typeSVG: "SVG",
    },
    fileImport: {
        doneButtonText: "Done",
        doneButtonTitle: "Finish importing data",
        fileUpload: "Open or Drop File",
        loadSample: "Load Sample Dataset...",
        links: "Links",
        messageNoID: function (keyColumn) {
            return "No " + keyColumn + " colum are specified in main table";
        },
        messageNoSourceOrTargetID: function (linkSourceKeyColumn, linkTargetKeyColumn) {
            return "No " + linkSourceKeyColumn + " or " + linkTargetKeyColumn + " colums are specified in links table";
        },
        removeButtonText: "Remove",
        removeButtonTitle: "Remove this table",
    },
    fileOpen: {
        copy: "Copy this chart",
        deleteConfirmation: function (chartName) {
            return "Do you want to delete the chart \"" + chartName + "\"?";
        },
        delete: "Delete this chart",
        download: "Download this chart",
        open: "Open Chart",
        noChart: "(no chart to show)",
    },
    fileSave: {
        saveButton: "Save to My Charts",
        chartName: "Chart Name",
    },
    filter: {
        editFilter: "Edit Filter",
        filterBy: "Filter by ",
        filterType: "Filter Type",
        none: "None",
        categories: "Categories",
        expression: "Expression",
        selectAll: "Select All",
        clear: "Clear",
        values: "Values",
        column: "Column",
    },
    handles: {
        drawSpiral: "Draw Spiral",
        startAngle: "Start Angle",
        windings: "Windings",
    },
    help: {
        contact: "Contact Us",
        gallery: "Example Gallery",
        gettingStarted: "Getting Started",
        home: "Charticulator Home",
        issues: "Report an Issue",
        version: function (version) { return "Version: " + version; },
    },
    mainTabs: {
        about: "About",
        export: "Export",
        new: "New",
        open: "Open",
        options: "Options",
        save: "Save As",
    },
    mainView: {
        attributesPaneltitle: "Attributes",
        datasetPanelTitle: "Dataset",
        errorsPanelTitle: "Errors",
        glyphPaneltitle: "Glyph",
        layersPanelTitle: "Layers",
        scalesPanelTitle: "Scales",
    },
    menuBar: {
        defaultTemplateName: "Charticulator Template",
        export: "Export",
        exportTemplate: "Export template",
        copyTemplate: "Copy template",
        help: "Help",
        home: "Open file menu",
        importTemplate: "Import template",
        new: "New (Ctrl-N)",
        open: "Open (Ctrl-O)",
        redo: "Redo (Ctrl-Y)",
        reset: "Delete",
        save: "Save (Ctrl-S)",
        saveButton: "Save",
        dontSaveButton: "Don't save",
        cancel: "Cancel",
        savedButton: "Saved",
        saveNested: "Save Nested Chart",
        editNestedChart: "Edit Nested Chart...",
        closeNested: "Close",
        undo: "Undo (Ctrl-Z)",
    },
    options: {
        comma: "comma",
        delimiter: "CSV Delimiter",
        fileFormat: "Import file format",
        numberFormat: "Number Format",
        timeZone: "Number Format",
        currencyFormat: "Currency Format",
        groups: "Groups",
        numberFormatComma: "Decimal: comma / Separator: dot",
        numberFormatDot: "Decimal: dot / Separator: comma",
        semicolon: "semicolon",
        utc: "UTC",
        local: "Local",
    },
    coordinateSystem: {
        x: "X",
        y: "Y",
    },
    templateImport: {
        columnNameTemplate: "Column name from the template",
        columnNameChart: "Column name from the chart design",
        dataType: "Required data type",
        examples: "Example data values",
        mapped: "Column name in the dataset",
        save: "Save mapping",
        tableName: "Table name",
        title: "Map your data",
        usbtitleImportTemplate: "Map the columns from your data source to the corresponding template fields",
        usbtitleImportData: "Map the columns from new data to the corresponding fields in the current chart design",
        unmapped: "Unmapped",
    },
    toolbar: {
        symbol: "Symbol",
        marks: "Marks",
        curve: "Custom Curve",
        dataAxis: "Data Axis",
        ellipse: "Ellipse",
        icon: "Icon",
        image: "Image",
        guides: "Guides",
        guidePolar: "Guide polar",
        guideX: "Guide X",
        guideY: "Guide Y",
        legend: "Legend",
        line: "Line",
        lineH: "Horizontal Line",
        lineV: "Vertical Line",
        link: "Link",
        links: "Links",
        nestedChart: "Nested Chart",
        plot: "Plot",
        plotSegments: "Plot Segments",
        polar: "Polar",
        rectangle: "Rectangle",
        region2D: "2D Region",
        scaffolds: "Scaffolds",
        text: "Text",
        textbox: "Textbox",
        triangle: "Triangle",
    },
    typeDisplayNames: {
        boolean: "Boolean",
        date: "Date",
        number: "Number",
        string: "String",
    },
    attributesPanel: {
        conditionedBy: "Conditioned by...",
    },
    core: {
        default: "(default)",
        auto: "(auto)",
        none: "(none)",
    },
    cartesianTerminology: cartesianTerminology,
    curveTerminology: curveTerminology,
    polarTerminology: polarTerminology,
    alignment: {
        align: "Align",
        alignment: "Alignment",
        left: "Left",
        right: "Right",
        middle: "Middle",
        center: "Center",
        top: "Top",
        bottom: "Bottom",
        padding: "Padding",
    },
    margins: {
        margins: "Margins",
        margin: "Margin:",
        left: "Left",
        right: "Right",
        top: "Top",
        bottom: "Bottom",
    },
    scale: {
        linear: "Linear",
        logarithmic: "Logarithmic",
    },
    objects: {
        default: "Default",
        opposite: "Opposite",
        position: "Position",
        general: "General",
        contextMenu: "Context menu",
        interactivity: "Interactivity",
        colors: "Colors",
        color: "Color",
        outline: "Outline",
        dimensions: "Dimensions",
        scale: "Scale",
        width: "Width",
        height: "Height",
        background: "Background",
        opacity: "Opacity",
        font: "Font",
        fontSize: "Font Size",
        size: "Size",
        axis: "Axis",
        style: "Style",
        rotation: "Rotation",
        anchorAndRotation: "Anchor & Rotation",
        fill: "Fill",
        strokeWidth: "Line Width",
        stroke: "Stroke",
        anchorX: "Anchor X",
        anchorY: "Anchor Y",
        alignX: "Align X",
        alignY: "Align Y",
        layout: "Layout",
        appearance: "Appearance",
        visibilityAndPosition: "Visibility & Position",
        onTop: "On Top",
        invalidFormat: "Invalid format",
        roundX: "Round X",
        roundY: "Round Y",
        dropData: "drop here to assign data",
        dropTickData: "Tick data: drop here to assign tick data",
        toolTips: "Tooltips",
        selection: "Selection",
        axes: {
            data: "Data",
            numericalSuffix: ": Numerical",
            categoricalSuffix: ": Categorical",
            stackingSuffix: ": Stacking",
            tickFormat: "Tick Format",
            tickData: "Tick Data",
            ticksize: "Tick Size",
            tickDataFormatType: "Tick Data Type",
            tickDataFormatTypeNone: "None",
            tickDataFormatTypeDate: "Date",
            tickDataFormatTypeNumber: "Number",
            from: "from",
            to: "to",
            gap: "Gap",
            direction: "Direction",
            count: "Count",
            dataExpressions: "Data Expressions",
            lineColor: "Line Color",
            tickColor: "Tick Label Color",
            tickTextBackgroudColor: "Tick background color",
            showTickLine: "Show Tick Line",
            showBaseline: "Show Baseline",
            verticalText: "Vertical text",
            offSet: "Offset",
            orderBy: "Order by",
            numberOfTicks: "Number of Ticks",
            autoNumberOfTicks: "Auto Number of Ticks",
        },
        plotSegment: {
            subLayout: "Sub-layout",
            type: "Type",
            gridline: "Gridline",
            polarCoordinates: "Polar Coordinates",
            heightToArea: "Height to Area",
            equalizeArea: "Equalize area",
            autoAlignment: "Automatic Alignment",
            origin: "Origin",
            inner: "Inner:",
            outer: "Outer:",
            radius: "Radius",
            angle: "Angle",
            curveCoordinates: "Curve Coordinates",
            normal: "Normal",
            groupBy: "Group by...",
            groupByCategory: "Group by ",
            distribution: "Distribution",
            gravity: "Gravity",
            packingInContainer: "Packing into container",
            packingX: "Packing X",
            packingY: "Packing Y",
            order: "Order",
            reverseGlyphs: "Reverse glyphs order",
            flipGrid: "Flip grid",
            orientation: "Orientation",
            direction: "Direction",
            directionDownRight: "Down Right",
            directionDownLeft: "Down Left",
            directionUpLeft: "Up Left",
            directionUpRight: "Up Right",
        },
        visibleOn: {
            visibility: "Visibility",
            label: "Visible On",
            all: "All",
            first: "First",
            last: "Last",
            visible: "Visible",
        },
        guides: {
            guideCoordinator: "Guide Coordinator",
            count: "Count",
            guide: "Guide",
            baseline: "Baseline",
            offset: "Offset",
            angular: "Angular",
            radial: "Radial",
            angle: "Angle",
        },
        legend: {
            orientation: "Orientation",
            vertical: "Vertical",
            horizontal: "Horizontal",
            legend: "Legend",
            editColors: "Edit scale colors",
            markerShape: "Shape",
            labels: "Labels",
            layout: "Layout",
            categoricalLegend: "Categorical legend",
            numericalColorLegend: "Numerical color legend",
            ordering: "Ordering",
        },
        links: {
            lineType: "Line Type",
            type: "Type",
            line: "Line",
            bezier: "Bezier",
            arc: "Arc",
            solid: "Solid",
            dashed: "Dashed",
            dotted: "Dotted",
            linkMarkType: "Line mark type",
            curveness: "Curveness",
            closeLink: "Close Link",
        },
        arrows: {
            beginArrowType: "Begin Arrow Type",
            endArrowType: "End Arrow Type",
            noArrow: "No Arrow",
            arrow: "Arrow",
            diamondArrow: "Diamond Arrow",
            ovalArrow: "Oval Arrow",
        },
        line: {
            lineStyle: "Line Style",
            xSpan: "X Span",
            ySpan: "Y Span",
        },
        anchor: {
            label: "(drag the anchor in the glyph editor)",
        },
        dataAxis: {
            dataExpression: "Data Expressions",
            autoUpdateValues: "Auto update values",
            autoMin: "Auto min value",
            autoMax: "Auto max value",
            end: "End",
            start: "Start",
            exportProperties: " export properties",
            domain: "Domain",
            range: "Range",
            gradient: "Gradient",
            scrolling: "Scrolling",
            allowScrolling: "Allow scrolling",
            windowSize: "Window size",
            barOffset: "Scrollbar offset",
        },
        icon: {
            label: "Icon",
            image: "Image",
            anchorAndRotation: "Anchor & Rotation",
            anchorX: "Anchor X",
            anchorY: "Anchor Y",
        },
        image: {
            imageMode: "Resize Mode",
            letterbox: "Letterbox",
            stretch: "Stretch",
            dropImage: "Drop Image Here",
            defaultPlaceholder: "Drop/Paste Image",
        },
        scales: {
            mode: "Mode",
            greater: "Greater",
            less: "Less",
            interval: "Interval",
            inclusive: "Inclusive",
            imageMapping: "Image Mapping",
            stringMapping: "String Mapping",
            colorMapping: "Color Mapping",
            numberMapping: "Number Mapping",
            booleanMapping: "Boolean Mapping",
            minimumValue: "Minimum value",
            maximumValue: "Maximum value",
            startDate: "Start date",
            endDate: "End date",
            exportProperties: "Scale export properties",
            autoMin: "Auto min value",
            autoMax: "Auto max value",
            selectAll: "Select All",
            clear: "Clear",
            value: "Value",
            date: "Date",
        },
        text: {
            margin: "Margin",
            wrapText: "Wrap text",
            overflow: "Overflow",
            textDisplaying: "Text displaying",
        },
        rect: {
            shape: "Shape",
            flipping: "Flipping",
            shapes: {
                rectangle: "Rectangle",
                triangle: "Triangle",
                ellipse: "Ellipse",
                comet: "Rounded base",
            },
        },
        derivedColumns: {
            year: "Year",
            month: "Month",
            monthNumber: "Month number",
            day: "Day",
            weekOfYear: "Week of year",
            dayOfYear: "Day of year",
            weekday: "Weekday",
            hour: "Hour",
            minute: "Minute",
            second: "Second",
            menuSuffix: " Derived columns ",
        },
        nestedChart: {
            sizeAndShape: "Size & Shape",
        },
    },
    reOrder: {
        reverse: "Reverse",
        sort: "Sort",
        reset: "Reset",
    },
    panels: {
        collapseAllCategories: "Collapse all categories",
        expandAllCategories: "Expand all categories",
    },
};
//# sourceMappingURL=strings.js.map