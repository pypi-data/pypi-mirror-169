"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
// Copyright (c) Microsoft Corporation. All rights reserved.
// Licensed under the MIT license.
var chai_1 = require("chai");
var container_1 = require("../../container");
var Expression = require("../../core/expression");
container_1.setTimeZone(true);
describe("Basic Expression", function () {
    var test_cases = [
        // Arithmetics
        ["1 - 2 - 3 - 4", -8],
        ["12 * (3 + 6 - 5 + 4 * (3 + 7)) * 13 / 12", 572],
        ["1 + 2 * 3 - 4 - (-7 + 5 * 6)", -20],
        ["-3 + 5", 2],
        ["-5^3", -125],
        ["--5^3", 125],
        ["3--5^3", 128],
        ["3-(-5)^3", 128],
        ["+--++-5", -5],
        ["a + b + sum(1,2,3,4) - (1+2-3*4)", 30],
        ["1 + 2 < 3 + 4", true],
        ["1 + 2 == 3 + 4 - 4", true],
        ["1 + 2 == 3 + 4", false],
        ["3 * 4 <= 4 * 3", true],
        ["3 > 1 and 5 < 8 ", true],
        ["not a == 1", false],
        ["true == (a == 1)", true],
        ["false == (a == 1)", false],
        ["min(1,2,3,4) == 1 and max(1,2,3,4,5) != 4", true],
        ["mean(1,2,3,4)", 2.5],
        ["value + 5", 13],
        ["mean(1,2,3,4)", 2.5],
        ["sum(map(range(1, 5), x => x * x))", 55],
        ['`test 1 \\t x\\"\\"` + 4', 6],
        ["date.month(date.parse(\"2014-12-14 11:23:45\"))", "Dec"],
        ["sum(json.parse(\"[12,13,14,16,1,2,3]\"))", 61],
        ["average(map(data, x => x.value))", 2],
        ["array(1,2,3,4) + array(5,6,7,8)", [6, 8, 10, 12]],
        ["stdev(list(100,150,100,125,125,150))", 20.412414523193135],
        ["variance(list(100,150,100,125,125,150))", 416.66666666666606],
        ["median(list(100,150,100,125,125,150))", 137.5],
    ];
    var context = new Expression.SimpleContext();
    context.variables = {
        a: 1,
        b: 10,
        value: 8,
        data: [
            { key: "A", value: 1 },
            { key: "B", value: 2 },
            { key: "C", value: 3 },
        ],
        'test 1 \t x""': 2,
    };
    it("getValue", function () {
        test_cases.forEach(function (ci) {
            var expr = ci[0];
            var expected = ci[1];
            var e = Expression.parse(expr);
            var returned = e.getValue(context);
            chai_1.expect(returned).deep.equals(expected, expr);
        });
    });
    it("toString", function () {
        test_cases.forEach(function (ci) {
            var expr = ci[0];
            var expected = ci[1];
            var e = Expression.parse(expr);
            var es = e.toString();
            var ep = Expression.parse(es);
            var epreturned = e.getValue(context);
            chai_1.expect(epreturned).deep.equals(expected, expr);
        });
    });
});
describe("Text Expression", function () {
    var test_cases = [
        [
            "Hello World, Temperature is ${Temperature}{.1f} degree",
            "Hello World, Temperature is 70.0 degree",
        ],
        ["\\$ ${Temperature}{.1f} \\\\F", "$ 70.0 \\F"],
    ];
    var context = new Expression.SimpleContext();
    context.variables = {
        Temperature: 70,
    };
    it("getValue", function () {
        test_cases.forEach(function (ci) {
            var expr = ci[0];
            var expected = ci[1];
            var e = Expression.parseTextExpression(expr);
            var returned = e.getValue(context);
            chai_1.expect(returned).deep.equals(expected, expr);
        });
    });
    it("toString", function () {
        test_cases.forEach(function (ci) {
            var expr = ci[0];
            var expected = ci[1];
            var e = Expression.parseTextExpression(expr);
            var es = e.toString();
            var ep = Expression.parseTextExpression(es);
            var epreturned = e.getValue(context);
            chai_1.expect(epreturned).deep.equals(expected, expr);
        });
    });
});
describe("Expression Utilities", function () {
    it("replace", function () {
        var cases = [
            ["a + b + c + d", { a: "A", b: "B" }, "A + B + c + d"],
            ["a + b * (c + d)", { a: "A", c: "C" }, "A + b * (C + d)"],
            ["a", { a: "A", b: "B" }, "A"],
        ];
        cases.forEach(function (ci) {
            chai_1.expect(Expression.parse(ci[0])
                .replace(Expression.variableReplacer(ci[1]))
                .toString()).equals(ci[2]);
        });
    });
    it("list_variables", function () {
        var cases = [
            ["a + b + c + d", ["a", "b", "c", "d"]],
            ["a + b * (c + d)", ["a", "b", "c", "d"]],
            ["a * (b + c) * d", ["a", "b", "c", "d"]],
        ];
        cases.forEach(function (ci) {
            var vars = new Set();
            Expression.parse(ci[0]).replace(function (expr) {
                if (expr instanceof Expression.Variable) {
                    vars.add(expr.name);
                }
            });
            var list = Array.from(vars).sort();
            chai_1.expect(list).deep.equals(ci[1]);
        });
    });
});
//# sourceMappingURL=expression.js.map