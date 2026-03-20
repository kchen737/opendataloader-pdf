import opendataloader_pdf

# Batch all files in one call — each convert() spawns a JVM process, so repeated calls are slow
opendataloader_pdf.convert(
    input_path=["numberabovepic.pdf", "metrics.pdf", "pure_words.pdf", "metrics_in_table.pdf" ,"testrun/"],
    output_dir="output/",
    format="markdown,json"
)

