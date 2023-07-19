export default function useDateFormat(dateString: string) {
  const date = new Date(dateString);

  const dayOfMonth = date.getDate();
  const formattedDayOfMonth = getFormattedDayOfMonth(dayOfMonth);

  const monthName = date.toLocaleString("default", { month: "long" });

  const year = date.getFullYear();

  const hours = date.getHours();
  const formattedHours = getFormattedHours(hours);

  const minutes = date.getMinutes();
  const formattedMinutes = getFormattedMinutes(minutes);

  const formattedDate = `${formattedDayOfMonth} ${monthName} ${year} - ${formattedHours}:${formattedMinutes}`;

  return formattedDate;
}

function getFormattedDayOfMonth(day: number) {
  if (day >= 11 && day <= 13) {
    return `${day}th`;
  } else {
    const lastDigit = day % 10;
    switch (lastDigit) {
      case 1:
        return `${day}st`;
      case 2:
        return `${day}nd`;
      case 3:
        return `${day}rd`;
      default:
        return `${day}th`;
    }
  }
}

function getFormattedHours(hours: number) {
  const formattedHours = hours % 12 || 12;
  return formattedHours < 10 ? `0${formattedHours}` : formattedHours;
}

function getFormattedMinutes(minutes: number) {
  return minutes < 10 ? `0${minutes}` : minutes;
}
