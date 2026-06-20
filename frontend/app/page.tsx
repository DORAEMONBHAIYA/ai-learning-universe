import Link from "next/link"
import { Button } from "@/components/ui/button"

const features = [
  {
    title: "AI Tutor",
    description: "Personalized tutoring powered by LLMs with RAG-based knowledge retrieval.",
  },
  {
    title: "Learning Roadmaps",
    description: "AI-generated personalized learning paths based on your goals.",
  },
  {
    title: "Smart Quizzes",
    description: "Adaptive quizzes that test and reinforce your understanding.",
  },
  {
    title: "Knowledge Graph",
    description: "Visualize how concepts connect and build on each other.",
  },
]

export default function Home() {
  return (
    <>
      <header className="sticky top-0 z-50 w-full border-b bg-background/95 backdrop-blur supports-[backdrop-filter]:bg-background/60">
        <div className="container mx-auto flex h-16 items-center justify-between px-4">
          <span className="text-xl font-bold">AI Learning Universe</span>
          <nav className="flex items-center gap-4">
            <Link href="/login">
              <Button variant="outline">Sign In</Button>
            </Link>
            <Link href="/login">
              <Button>Get Started</Button>
            </Link>
          </nav>
        </div>
      </header>

      <main className="flex-1">
        <section className="container mx-auto flex flex-col items-center gap-8 px-4 py-24 text-center">
          <h1 className="max-w-3xl text-4xl font-bold tracking-tight sm:text-5xl md:text-6xl">
            Learn Anything with Your
            <span className="text-primary"> AI Tutor</span>
          </h1>
          <p className="max-w-2xl text-lg text-muted-foreground">
            AI Learning Universe combines LLMs, knowledge graphs, and adaptive learning to create
            a personalized education experience tailored to your goals.
          </p>
          <div className="flex gap-4">
            <Link href="/login">
              <Button size="lg">Start Learning Free</Button>
            </Link>
            <Link href="/login">
              <Button variant="outline" size="lg">
                Watch Demo
              </Button>
            </Link>
          </div>
        </section>

        <section className="container mx-auto grid gap-6 px-4 pb-24 sm:grid-cols-2 lg:grid-cols-4">
          {features.map((feature) => (
            <div
              key={feature.title}
              className="rounded-lg border bg-card p-6 text-card-foreground shadow-sm transition-shadow hover:shadow-md"
            >
              <h3 className="mb-2 text-lg font-semibold">{feature.title}</h3>
              <p className="text-sm text-muted-foreground">{feature.description}</p>
            </div>
          ))}
        </section>
      </main>

      <footer className="border-t py-6 text-center text-sm text-muted-foreground">
        &copy; {new Date().getFullYear()} AI Learning Universe. Built with FastAPI, Next.js, and OpenRouter.
      </footer>
    </>
  )
}
