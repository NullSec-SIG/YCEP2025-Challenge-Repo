"use client"

export default function Admin() {
    return (
        <>
            <script type="text/javascript">
                window.location.href = "/notauthorised"
            </script>
            <div className="flex flex-col items-center justify-center min-h-[calc(100svh-60px)]">
                <h1>Admin Panel</h1>
                <h4 className="text-secondary" style={{ marginTop: "10px" }}>Please login using your issued passkey to continue.</h4>
                <img src="qr-code.png" className="w-[15%]" style={{ paddingTop: "20px" }}/>
                <div className="absolute bottom-0 w-full flex items-center justify-center py-4 text-secondary">
                    <p className="text-secondary">Powered by Azure Active Directory. Read the documentation <a href="https://go.microsoft.com/fwlink/?LinkId=856642" target="blank" style={{ color: "#0000EE" }}>here</a>.</p>
                </div>
            </div>
        </>
    )
}