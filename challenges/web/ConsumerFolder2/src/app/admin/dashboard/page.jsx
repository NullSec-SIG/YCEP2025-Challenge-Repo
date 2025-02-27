export default function Dashboard() {
    return (
        <>
        <div className="flex flex-col items-center justify-center min-h-[calc(100svh-60px)]">
            <h1>Admin Dashboard</h1>
            <h2 style={{ marginTop: "10px" }}>{"YCEP25{t1m3_t0_f1r3_th3_1nt3rn}"}</h2>
            <div className="absolute bottom-0 w-full flex items-center justify-center py-4 text-secondary">
            <p className="text-secondary">Proudly powered by Next.js and independent of SQLite.</p>
            </div>
        </div>
        </>
    )
}