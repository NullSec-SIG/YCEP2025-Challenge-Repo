"use client"
import { useState, useEffect } from "react";

export default function Countdown() {

    const [time, setTime] = useState({
        years: 0,
        months: 0,
        days: 0,
        hours: 0,
        minutes: 0,
        seconds: 0
    });

    useEffect(() => {
        const interval = setInterval(() => {
            const targetDate = new Date("1965-08-09T00:00:00.000");
            const currentDate = new Date();
            const difference = currentDate - targetDate;

            const years = Math.floor(difference / (1000 * 60 * 60 * 24 * 365));
            const months = Math.abs(currentDate.getMonth() - targetDate.getMonth());
            const monthOnly = new Date(targetDate.getFullYear(), targetDate.getMonth(), 0);
            var days = currentDate.getDate() - monthOnly.getDate()
            if (days < 0)
                days = (((currentDate.getDate() - targetDate.getDate()) % monthOnly.getDate()) + monthOnly.getDate()) % monthOnly.getDate();
            const hours = (((currentDate.getHours() - targetDate.getHours()) % 24) + 24) % 24;
            const minutes = (((currentDate.getMinutes() - targetDate.getMinutes()) % 60) + 60) % 60;
            const seconds = (((currentDate.getSeconds() - targetDate.getSeconds()) % 60) + 60) % 60;

            setTime({ years, months, days, hours, minutes, seconds });
        }, 1000);

        return () => clearInterval(interval);
    }, []);

    return (
        <>
            <div className="flex flex-row items-start justify-between">
                <div className="flex flex-col items-center border-1 border-gray-200 shadow-xl rounded-lg p-4 ms-4 w-26">
                    <h1 id="years" className="text-primary">{time.years}</h1>
                    <h6 className="text-secondary">YEARS</h6>
                </div>
                <div className="flex flex-col items-center border-1 border-gray-200 shadow-xl rounded-lg p-4 ms-4 w-26">
                    <h1 id="months" className="text-primary">{time.months}</h1>
                    <h6 className="text-secondary">MONTHS</h6>
                </div>
                <div className="flex flex-col items-center border-1 border-gray-200 shadow-xl rounded-lg p-4 ms-4 w-26">
                    <h1 id="days" className="text-primary">{time.days}</h1>
                    <h6 className="text-secondary">DAYS</h6>
                </div>
                <div className="flex flex-col items-center border-1 border-gray-200 shadow-xl rounded-lg p-4 ms-4 w-26">
                    <h1 id="hours" className="text-primary">{time.hours}</h1>
                    <h6 className="text-secondary">HOURS</h6>
                </div>
                <div className="flex flex-col items-center border-1 border-gray-200 shadow-xl rounded-lg p-4 ms-4 w-26">
                    <h1 id="minutes" className="text-primary">{time.minutes}</h1>
                    <h6 className="text-secondary">MINUTES</h6>
                </div>
                <div className="flex flex-col items-center border-1 border-gray-200 shadow-xl rounded-lg p-4 ms-4 w-26">
                    <h1 id="seconds" className="text-primary">{time.seconds}</h1>
                    <h6 className="text-secondary">SECONDS</h6>
                </div>
            </div>
        </>
    )
}