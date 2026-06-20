const API_URL = process.env.NEXT_PUBLIC_API_URL || "http://localhost:8000"

export class ApiError extends Error {
  constructor(
    public status: number,
    message: string,
  ) {
    super(message)
    this.name = "ApiError"
  }
}

async function request<T>(
  endpoint: string,
  options: RequestInit = {},
): Promise<T> {
  const url = `${API_URL}${endpoint}`

  const res = await fetch(url, {
    ...options,
    headers: {
      "Content-Type": "application/json",
      ...options.headers,
    },
  })

  if (!res.ok) {
    const body = await res.json().catch(() => ({}))
    throw new ApiError(res.status, body.detail || body.error || "Request failed")
  }

  return res.json()
}

export function authHeaders(token: string): HeadersInit {
  return { Authorization: `Bearer ${token}` }
}

export const api = {
  get: <T>(endpoint: string, token?: string) =>
    request<T>(endpoint, { headers: token ? authHeaders(token) : undefined }),

  post: <T>(endpoint: string, body: unknown, token?: string) =>
    request<T>(endpoint, {
      method: "POST",
      body: JSON.stringify(body),
      headers: token ? authHeaders(token) : undefined,
    }),
}
