export default function useColorGenerator() {
  // Generate random numbers for R, G, and B values
  const r = Math.floor(Math.random() * 256);
  const g = Math.floor(Math.random() * 256);
  const b = Math.floor(Math.random() * 256);

  // Build the CSS color string
  const color = `rgb(${r}, ${g}, ${b})`;

  return color;
}
