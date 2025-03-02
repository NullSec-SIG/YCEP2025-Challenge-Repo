"use client"
import Button from 'react-bootstrap/Button';
import Form from 'react-bootstrap/Form';
import React, { useEffect, useState } from 'react';
import cookieCutter from "@boiseitguru/cookie-cutter";

export default function Admin() {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [invalidCredsClass, setInvalidCredsClass] = useState("mb-4 collapse");
  const [Users, setUsers] = useState({});

  const usernameField = React.createRef();
  const passwordField = React.createRef();

  useEffect(() => {
    const fetchData = async () => {
      const data = await fetch('/page.json')
      const posts = await data.json()
      console.log(posts)
      setUsers(posts)
    }
    fetchData();
  }, [])

  const onSubmit = () => {
    for (const [key, value] of Object.entries(Users)) {
      if (key === username && atob(value[0]) === password && value[1] === true) {
        cookieCutter.set("user", username)
        cookieCutter.set("password", btoa(password))
        return window.location.href = "/admin/dashboard"
      }
    }
    usernameField.current.value = "";
    passwordField.current.value = "";
    return setInvalidCredsClass("mb-4");
  }

  return (
    <>
      <div className="flex flex-col items-center justify-center min-h-[calc(100svh-60px)]">
        <h1>Admin Panel</h1>
        <h4 className="text-secondary" style={{ marginTop: "10px" }}>Please login using valid ConsumerFolder credentials to continue.</h4>
        <Form className="w-3xl mt-4 mb-4">
          <Form.Group className="mb-3" controlId="username">
            <Form.Label>Username</Form.Label>
            <Form.Control ref={usernameField} size="lg" type="text" placeholder="Username" onChange={(e) => setUsername(e.target.value)} />
          </Form.Group>
          <Form.Group className="mb-3" controlId="password">
            <Form.Label>Password</Form.Label>
            <Form.Control ref={passwordField} size="lg" type="password" placeholder="Password" onKeyUp={(e) => (e.key === "Enter") ? onSubmit() : null} onChange={(e) => setPassword(e.target.value)} />
          </Form.Group>
        </Form>
        <h4 className={invalidCredsClass} style={{ color: "red" }}>Invalid credentials.</h4>
        <Button size="lg" type="submit" onClick={onSubmit}>Sign in</Button>
        <div className="absolute bottom-0 w-full flex items-center justify-center py-4 text-secondary">
          <p className="text-secondary">Proudly powered by Next.js and independent of SQLite.</p>
        </div>
      </div>
    </>
  )
}