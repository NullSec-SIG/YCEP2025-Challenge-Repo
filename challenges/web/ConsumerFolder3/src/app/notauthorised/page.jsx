export default function NotAuthorised() {
    return (
        <>
            <div className="flex flex-col items-center justify-center min-h-[calc(100svh-60px)]">
                <h1>403 Not Authorised</h1>
                <h4 style={{ marginTop: "10px" }} className="text-secondary">You are not authorised to view this page.</h4>
            </div>
        </>
    )
}