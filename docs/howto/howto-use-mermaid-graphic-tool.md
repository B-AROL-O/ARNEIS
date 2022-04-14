# HOWTO Mermaid utilisation and code examples

[Mermaid](https://mermaid-js.github.io/mermaid/#/) is a useful tool to create diagrams and charts directly using [Markdown](https://daringfireball.net/projects/markdown/).
The good part about it is that those diagrams can be easily modified just by changing a code displayed before the image, however we can't just move the image wherever we want to.
For this reason the [online tool](https://mermaid-js.github.io/mermaid-live-editor/edit#pako:eNpdj70OgzAMhF8Feaxg6ZihS9uxE2PDYBEDkfJTBQepQrx7UwJSi6fTd2fLN0PrFYGAkZHpprEPaKvpLF2R5nlqiqq6FDVrYzJa5QqTeUQPP2nXZ5r1cf2HXgOOQ6ar_D-6D5RgKVjUKj05fz0JPJAlCSJJRR1GwxKkW1I0vlSqcVeafQDRoRmpBIzs67drQXCItIe2rltq-QCq71E-) is better in case we are just interested in the results.

In order to create a mermaid graph:

* Use the bash code (```bash```) and instead of writing "bash" write "mermaid".
* write the code of the diagram (the diagram syntax can be find [here](https://mermaid-js.github.io/mermaid/#/), where all the kinds of diagram are stated with examples and codes)
* as a result, the graph will appear. There are a lot of configurable settings like the background or the color of the boxes. Everything can be found in their [site](https://mermaid-js.github.io/mermaid/#/).

## Example

```mermaid
graph TD;
    A-->B;
    A-->C;
    B-->D;
    C-->D;
```

NOTE: be careful, the background of the diagram depends on the style chosen on GitHub. So if you have the dark theme, it will be dark, making the diagram not
understandable. They are trying to implement a new [feature to solve this problem](https://github.com/mermaid-js/mermaid/issues/1553) but for now I suggest you to use
the theme dark in the code by using ```%%{init:{'theme':'dark'}}%%``` at the beginning of the code (on their site it is well explained and there are multiple examples).

<!-- EOF -->

