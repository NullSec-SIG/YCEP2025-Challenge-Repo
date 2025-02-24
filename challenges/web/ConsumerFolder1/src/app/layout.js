"use client"

import { Geist, Geist_Mono } from "next/font/google";
import "./globals.css";

import Container from 'react-bootstrap/Container';
import Nav from 'react-bootstrap/Nav';
import Navbar from 'react-bootstrap/Navbar';
import NavDropdown from 'react-bootstrap/NavDropdown';

const geistSans = Geist({
  variable: "--font-geist-sans",
  subsets: ["latin"],
});

const geistMono = Geist_Mono({
  variable: "--font-geist-mono",
  subsets: ["latin"],
});

export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <title>ConsumerFolder</title>
      <body className={`${geistSans.variable} ${geistMono.variable}`}>
        <Navbar expand="lg" className="bg-body-tertiary" bg="dark" data-bs-theme="dark">
          <Container>
            <Navbar.Brand href="/">ConsumerFolder</Navbar.Brand>
            <Nav className="ms-auto">
              <Nav.Link href="/records">Search Records</Nav.Link>
            </Nav>
          </Container>
        </Navbar>
        {children}
      </body>
    </html>
  );
}
