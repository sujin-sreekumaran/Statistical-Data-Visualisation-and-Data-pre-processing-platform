import jwt from "jsonwebtoken";
import multer from "multer";
import { promisify } from "util";

// Configure multer for file upload
const upload = multer({ dest: "uploads/" });

// Promisify multer middleware
const runMiddleware = promisify(upload.single("file"));

export const config = {
  api: {
    bodyParser: false,
  },
};

export default async function handler(req, res) {
  switch (req.method) {
    case "POST":
      if (req.url.endsWith("/login")) {
        return handleLogin(req, res);
      } else if (req.url.endsWith("/signup")) {
        return handleSignup(req, res);
      } else if (req.url.endsWith("/upload")) {
        return handleFileUpload(req, res);
      }
      break;
    default:
      res.setHeader("Allow", ["POST"]);
      res.status(405).end(`Method ${req.method} Not Allowed`);
  }
}

function handleLogin(req, res) {
  // Implement login logic here
  // Verify credentials, create JWT token, etc.
}

function handleSignup(req, res) {
  // Implement signup logic here
  // Create new user, create JWT token, etc.
}

async function handleFileUpload(req, res) {
  try {
    await runMiddleware(req, res);
    // File is now available in req.file
    // Implement file saving logic here
    res.status(200).json({ message: "File uploaded successfully" });
  } catch (error) {
    res.status(500).json({ message: "Error uploading file" });
  }
}

function verifyToken(token) {
  try {
    return jwt.verify(token, process.env.JWT_SECRET);
  } catch (error) {
    return null;
  }
}
