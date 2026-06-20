import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card"

export default function DashboardPage() {
  return (
    <main className="container mx-auto flex-1 px-4 py-8">
      <h1 className="mb-8 text-3xl font-bold">Dashboard</h1>
      <div className="grid gap-6 sm:grid-cols-2 lg:grid-cols-3">
        <Card>
          <CardHeader>
            <CardTitle className="text-lg">Topics Mastered</CardTitle>
          </CardHeader>
          <CardContent>
            <p className="text-3xl font-bold">0</p>
          </CardContent>
        </Card>
        <Card>
          <CardHeader>
            <CardTitle className="text-lg">Quiz Score</CardTitle>
          </CardHeader>
          <CardContent>
            <p className="text-3xl font-bold">—</p>
          </CardContent>
        </Card>
        <Card>
          <CardHeader>
            <CardTitle className="text-lg">Current Streak</CardTitle>
          </CardHeader>
          <CardContent>
            <p className="text-3xl font-bold">0 days</p>
          </CardContent>
        </Card>
      </div>
    </main>
  )
}
