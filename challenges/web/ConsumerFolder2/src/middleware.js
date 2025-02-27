import { NextResponse } from 'next/server'

export async function middleware(request) {
    const user = request.cookies.get("user")?.value ?? ""
    const password = request.cookies.get("password")?.value ?? ""
    const pathName = request.nextUrl.pathname

    if (pathName === "/admin/dashboard") {
        if (user === "radeon" && password === "bmV2ZXJfbWlzc19hbl9vcHBvcnR1bml0eV90b19taXNzX2FuX29wcG9ydHVuaXR5") {
            return NextResponse.next()
        }
        return NextResponse.redirect(new URL("/notauthorised", request.nextUrl))
    }

    const response = NextResponse.next()
    response.cookies.delete("user")
    response.cookies.delete("password")
    return response
}