use anyhow::Result;

use plotly::common::Mode;
use plotly::{Plot, Scatter};

fn main() -> Result<()> {
    plot_line_and_scatter();
    Ok(())
}

fn plot_line_and_scatter() {
    let trace1 = Scatter::new(vec![1f32, 2., 3., 4.], vec![10f32, 15., 13., 17.])
        .name("trace1")
        .mode(Mode::Markers);
    let trace2 = Scatter::new(vec![2f32, 3., 4., 5.], vec![16f32, 5., 11., 9.])
        .name("trace2")
        .mode(Mode::Lines);
    let trace3 = Scatter::new(vec![1., 3., 4., 5.], vec![12f32, 9., 15., 12.]).name("trace3");

    let mut plot = Plot::new();
    plot.add_trace(trace1);
    plot.add_trace(trace2);
    plot.add_trace(trace3);

    //plot.show();
    // plot.save("filename", ImageFormat::PNG, width, height, scale);
    plot.to_html("out.html");
}
