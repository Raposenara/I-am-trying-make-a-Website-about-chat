// app/layout.tsx
export const metadata = {
  title: "Meu Chat",
  description: "Aplicativo de chat usando Next.js",
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  );
}
