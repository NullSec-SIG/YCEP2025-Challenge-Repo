"use client"

import Alert from 'react-bootstrap/Alert';
import Button from "react-bootstrap/Button";
import Countdown from "@/components/countdown";
import { IoIosInformationCircle } from "react-icons/io";

export default function Home() {
  return (
    <>
      <div className={`flex flex-col items-center min-h-svh`} style={{ paddingBottom: "150px" }}>
        <Alert variant="info" style={{ marginTop: "30px" }}>
          <Alert.Heading>
            <div className="flex flex-row items-center w-full font-semibold">
              <IoIosInformationCircle style={{ width: "30px", height: "30px", marginRight: "1%", marginTop: "2px" }} />
              Patch 1.0.2
            </div>
          </Alert.Heading>
          <hr />
          <p className="max-w-[1120px]">In light of some recent allegations of an alleged data breach, we would like to deny all responsibility and say that it wasn't our fault, nor was it a data breach.
          <br />
          <br />
          See, it was a feature, not a bug. NRICs have totally never ever been secret nor treated like such at all. Not a doubt. It is a new completely unannounced government policy
          we totally didn't just make up to cover our asses and avoid the bad PR, and we simply jumped the gun before they announced it. We are "sorry" for the "confusion".
          <br />
          <br />
          Oh and yeah, the bug which isn't a bug but that we fixed anyway has been patched, so yeah, enjoy.</p>
        </Alert>
        <img style={{ margin: "20px" }} src="professional-man-searching-laptop-data.jpg" />
        <h1 style={{ fontSize: "2.2rem" }}>Entrusted with the <span style={{ color: "red" }}><strong>insensitive*</strong></span> personal data of</h1>
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
