"use client"; // Adicione esta linha

import { useState, useEffect } from "react";
import { io } from "socket.io-client";

export default function Home() {
  const [messages, setMessages] = useState<string[]>([]);
  const [newMessage, setNewMessage] = useState("");

  useEffect(() => {
    const socket = io("http://localhost:3001"); // URL do servidor do socket.io
    socket.on("message", (message: string) => {
      setMessages((prevMessages) => [...prevMessages, message]);
    });

    return () => {
      socket.disconnect();
    };
  }, []);

  const sendMessage = () => {
    // Aqui você enviaria a mensagem pelo socket.io
    console.log("Mensagem enviada:", newMessage);
    setNewMessage(""); // Limpa o campo após envio
  };

  return (
    <div>
      <h1>Chat App</h1>
      <div>
        {messages.map((message, index) => (
          <p key={index}>{message}</p>
        ))}
      </div>
      <input
        type="text"
        value={newMessage}
        onChange={(e) => setNewMessage(e.target.value)}
      />
      <button onClick={sendMessage}>Enviar</button>
    </div>
  );
}
