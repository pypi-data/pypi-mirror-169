/// <reference types="hammerjs" />
import * as React from "react";
export interface ScrollViewState {
    height: number;
    position: number;
}
export declare class ScrollView extends React.Component<Record<string, unknown>, ScrollViewState> {
    refs: {
        container: HTMLDivElement;
    };
    hammer: HammerManager;
    componentDidMount(): void;
    componentWillUnmount(): void;
    render(): JSX.Element;
}
