// Load the Observable runtime and inspector.

import {Runtime, Inspector} from "https://cdn.jsdelivr.net/npm/@observablehq/runtime@4/dist/runtime.js";

// Your notebook, compiled as an ES module.
import notebook from "https://api.observablehq.com/@c6eff9e0b1e718b7/user-reaction-to-joe-bidens-tweets-2021.js?v=3";

// Load the notebook, observing its cells with a default Inspector that simply renders the value of each cell into the provided DOM node.
new Runtime().module(notebook, Inspector.into(document.body));

//to render just the cell named “chart” into the DOM element with the same id, say:

new Runtime().module(notebook, name => {
  if (name === "chart") {
    return new Inspector(document.querySelector("#chart"));
  }
});
