import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI();
const response = await ai.models.generateContent({
  model: "gemma-4-26b-a4b-it",
  contents: "Explain open source in 3 sentences.",
});

console.log(response.text);
