"use client"

import Button from "react-bootstrap/Button";
import Countdown from "@/components/countdown";

export default function Home() {
  return (
    <>
      <div className={`flex flex-col items-center min-h-svh`} style={{ paddingBottom: "150px" }}>
        <img style={{ margin: "50px" }} src="professional-man-searching-laptop-data.jpg" />
        <h1 style={{ fontSize: "2.2rem" }}>Entrusted with the personal data of</h1>
        <h1 className="text-2xl">over <strong>6,036,900</strong> Singaporeans.</h1>
        <div className="flex flex-row items-center">
          <Button href="/records" style={{ marginTop: "20px" }} variant="primary" size="lg">Get Started</Button>
          <Button href="#learn-more" style={{ marginTop: "20px", marginLeft: "20px" }} variant="secondary" size="lg">Learn More</Button>
        </div>
      </div>
      <div id="learn-more" className="flex flex-row justify-between" style={{ paddingLeft: "10%", paddingRight: "10%" }}>
        <div className="flex flex-col min-h-100">
          <h1 style={{ fontSize: "2.25rem" }}>Need to find someone, something, somewhere in Singapore?</h1>
          <h1 style={{ fontSize: "2.25rem" }}><strong>We got you.</strong></h1>
          <h4 className="text-secondary">Storing local records dating back to <strong>9 August, 1965.</strong></h4>
        </div>
        <Countdown />
      </div>
      <div className="flex flex-row items-center justify-between" style={{ paddingLeft: "10%", paddingRight: "10%", marginBottom: "150px" }}>
        <img className="w-md" src="Designer.jpeg" />
        <div className="flex flex-col">
          <h1 className="text-right">Data breaches?</h1>
          <h1 className="text-right"><strong>Never heard of them.</strong></h1>
          <h4 className="text-secondary text-right">Equipped with bulletproof cybersecurity, ConsumerFolder is an <strong>impregnable fortress.</strong></h4>
          <h4 className="text-secondary text-right">Imagine leaking everyone's NRIC due to poor access control. 100% not with us.</h4>
        </div>
      </div>
      <h1 className="w-1/2 mx-auto my-0 text-center" style={{ paddingBottom: "50px" }}>Testimonials</h1>
      <div className="flex flex-row items-center justify-between" style={{ paddingLeft: "10%", paddingRight: "10%", paddingBottom: "150px" }}>
          <div className="flex flex-col w-full">
            <h1 className="text-left">Daksh (web penetration tester)</h1>
            <h4 className="text-secondary text-left text-wrap max-w-[90%]" style={{ lineHeight: "40px" }}>
              "As a web penetration tester, I was taken aback by the <strong>impressive cybersecurity measures</strong> that went into the creation of ConsumerFolder. Despite my best efforts, I was <strong>completely unable</strong>
              <strong> to breach their defenses</strong> and <strong>totally didn't sell all the breached data to the dark web.</strong>"
              </h4>
          </div>
          <img src="daksh.webp" className="w-2xs" />
        </div>
      <div className="flex flex-col items-center justify-center" style={{ marginBottom: "150px" }}>
        <h1>So what are you waiting for?</h1>
        <h4 className="text-secondary">Dive into our wealth of government records now.</h4>
        <Button href="/records" style={{ marginTop: "20px" }} variant="primary" size="lg">Get Started</Button>
      </div>
    </>
  )
}
