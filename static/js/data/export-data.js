const modelSelect = document.getElementById("model-name");
const previewBox = document.getElementById("exportPreviewBox");
const previewSubtitle = document.getElementById("previewSubtitle");
const csvFileName = document.getElementById("csvFileName");

if (modelSelect) {
  modelSelect.addEventListener("change", (e) => {
    const selectedModel = e.target.value;
    if (selectedModel) {
      previewBox.classList.add("active");
      previewSubtitle.textContent = `All records from "${selectedModel}" table will be exported`;
      csvFileName.textContent = `${selectedModel.toLowerCase()}_data.csv`;
    }
  });
}
