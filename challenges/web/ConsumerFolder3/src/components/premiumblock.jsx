import Button from "react-bootstrap/Button";

export default function PremiumBlock({ visibility }) {
    return (
        <div className={`flex flex-col items-center justify-center absolute h-full ${visibility ? "visible" : "collapse"}`} style={{ marginBottom: "150px", maxWidth: "600px", top: "2%", right: "6.5%" }}>
            <h1>Secret User Profile 😱</h1>
            <h4 style={{ marginTop: "10px" }} className="text-secondary">This user bribed us $5000 not to reveal his profile.</h4>
            <h4 className="text-secondary">Double it up, pay us $10,000 if you wanna see it.</h4>
            <div className="flex flex-row items-center justify-center" style={{ marginTop: "20px" }}>
                <Button href="/toopoor" variant="primary" size="lg" style={{ marginRight: "20px" }}>Pay and Unlock</Button>
                <Button href="/admin" variant="danger" size="lg">Admin Panel</Button>
            </div>
        </div>
    )
}