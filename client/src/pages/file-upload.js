import { useState } from "react";
import axios from "axios";

export default function UploadFile() {
  const [file, setFile] = useState(null); // Store the selected file
  const [imageURL, setImageURL] = useState(""); // Store the URL of the generated image

  // Function to handle file input change
  const handleFileChange = (e) => {
    setFile(e.target.files[0]);
  };

  // Function to handle form submission
  const handleSubmit = async (e) => {
    e.preventDefault();

    if (!file) {
      alert("Please upload a file");
      return;
    }

    const formData = new FormData();
    formData.append("file", file); // Append the file to the FormData

    try {
      // Send file to Flask backend
      const response = await axios
        .post("http://127.0.0.1:5000/upload", formData, {
          headers: {
            "Content-Type": "multipart/form-data",
          },
          responseType: "blob", // Expecting a blob (image) in the response
        })
        .catch((error) => {
          console.error("Error uploading the file", error);
        });

      // Create a URL for the image blob and set it as the image source
      const imageBlob = new Blob([response.data], { type: "image/png" });
      const imageURL = URL.createObjectURL(imageBlob);
      setImageURL(imageURL); // Update the state with the image URL
    } catch (error) {
      console.error("Error uploading the file", error);
    }
  };

  return (
    <div>
      <form onSubmit={handleSubmit}>
        <input type="file" accept=".csv, .xlsx" onChange={handleFileChange} />{" "}
        {/* Accept CSV and Excel files */}
        <button type="submit">Upload File</button>
      </form>

      {/* Display the image */}
      {imageURL && (
        <div>
          <h3>Generated Visualizations:</h3>
          <img
            src={imageURL}
            alt="Data Visualization"
            style={{ marginTop: "20px", maxWidth: "100%" }}
          />
        </div>
      )}
    </div>
  );
}
