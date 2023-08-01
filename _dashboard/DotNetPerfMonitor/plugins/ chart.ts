import { Bar, Line } from "vue-chartjs";
import {
  Chart as ChartJS,
  Title,
  Tooltip,
  Legend,
  BarElement,
  LineElement,
  CategoryScale,
  LinearScale,
  LogarithmicScale,
  TimeSeriesScale,
  TimeScale,
  PointElement,
} from "chart.js";

ChartJS.register(
  Title,
  Tooltip,
  Legend,
  BarElement,
  CategoryScale,
  TimeScale,
  TimeSeriesScale,
  LineElement,
  LogarithmicScale,
  PointElement,
  LinearScale
);

export default defineNuxtPlugin((nuxtApp) => {
  nuxtApp.vueApp.component("LineChart", Line);
  nuxtApp.vueApp.component("BarChart", Bar);
});
