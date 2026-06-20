export interface User {
  id: string
  email: string
  name: string | null
  avatar_url: string | null
  is_active: boolean
  created_at: string
}

export interface UserProfile {
  id: string
  user_id: string
  learning_style: string | null
  experience_level: string | null
  goals: string[]
  target_role: string | null
}

export interface AuthResponse {
  access_token: string
  token_type: string
  user: User
  profile: UserProfile | null
}

export interface ApiResponse<T> {
  data?: T
  error?: string
  detail?: string
}
