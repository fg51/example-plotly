from plotly import graph_objects as go


def main() -> None:
    fig = go.Figure()

    fig.add_trace(
        go.Scatter(
            mode="markers+lines",
            x=list(stub()),
            y=[i * 2 for i in stub()],
            name="sample",
            opacity=0.7,
            showlegend=True,
        )
    )

    fig.update_layout(
        title="title",
        xaxis=dict(
            title="x",
            range=[-10, 10],
            # tickformat="%y %b",
            # dtick="M4",
            # type="log",
        ),
        yaxis=dict(
            title="y",
            range=[-20, 20],
            # dtick=100,
        ),
        legend=dict(
            x=0.01,
            y=0.99,
            xanchor="left",
            yanchor="top",
            bgcolor="rgba(255, 255, 255, 0.5)",
            # orientation="h",
        ),
        # plot_bgcolor="white",
    )
    # fig.update_xaxes(title="xx", showline=True, linewidth=True, linecolor='lightgrey', color='grey')
    # fig.update_yaxes(title="yy", showline=True, linewidth=True, linecolor='lightgrey', color='grey')
    fig.add_annotation(
        text="<b>annotation</b>",
        showarrow=True,
        x=3,
        y=6,
        align="left",
        font=dict(size=18, color="blue"),
    )

    fig.write_html("out.html")


def stub():
    for i in range(4):
        yield i + 1


if __name__ == "__main__":
    main()
