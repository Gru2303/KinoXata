// This file is auto-generated by @hey-api/openapi-ts

export type AdminStatsResponse = {
  users: number
  films: number
  sessions: number
  tickets_sell: number
  month_money: number
  week_money: number
}

export type AdminUserRequest = {
  limit?: number | null
  offset?: number | null
}

export type AdminUserSetRequest = {
  id: number
  admin: boolean
}

export type ErrorResponse = {
  message: string
}

export type GoogleLoginResponse = {
  url: string
}

export type HTTPValidationError = {
  detail?: Array<ValidationError>
}

export type MovieAddRequest = {
  title: string
  description: string
  image: string
  afisha_image: string
  lang: string
  genre: string
  time: string
  trailer: string
  price: number
}

export type MovieRequest = {
  id: number
}

export type MovieResponse = {
  id: number
  title: string
  description: string
  image: string
  afisha_image: string
  lang: string
  genre: string
  time: string
  trailer: string
  price: number
  create_time: Date
  update_time: Date
}

export type MovieSessionRequest = {
  id: number
}

export type MovieSessionsAddRequest = {
  film_id: number
  seats: number
  date: Date
}

export type MovieSessionsRequest = {
  id: number
}

export type MovieSessionsResponse = {
  id: number
  film_id: number
  seats: number
  seats_busy: string
  date: Date
  create_time: Date
  update_time: Date
}

export type MoviesRequest = {
  limit?: number | null
  offset?: number | null
}

export type MoviesSessionsAdminRequest = {
  limit?: number | null
  offset?: number | null
}

export type PaymentProcessRequest = {
  session_id: number
  seats: Array<number>
  card_number: string
  card_name: string
  card_exp: string
  card_cvv: string
}

export type PaymentProcessResponse = {
  success: boolean
  message?: string | null
}

export type UserMeResponse = {
  id: number
  email: string
  name: string
  picture: string
  permission: string
  register_time: Date
}

export type UserTicketResponse = {
  id: number
  film: MovieResponse
  seats: Array<number>
  date: Date
  secret: string
}

export type UserTicketSignRequest = {
  sign: string
}

export type ValidationError = {
  loc: Array<string | number>
  msg: string
  type: string
}

export type GetGoogleLoginUrlResponse = GoogleLoginResponse

export type GetGoogleLoginUrlError = unknown

export type GoogleLoginCallbackData = {
  query?: {
    code?: string | null
  }
}

export type GoogleLoginCallbackResponse = unknown

export type GoogleLoginCallbackError = ErrorResponse | HTTPValidationError

export type UnauthorizedResponse = unknown

export type UnauthorizedError = unknown

export type GetMoviesData = {
  body?: MoviesRequest | null
}

export type GetMoviesResponse = Array<MovieResponse>

export type GetMoviesError = HTTPValidationError

export type GetMovieData = {
  body: MovieRequest
}

export type GetMovieResponse = MovieResponse

export type GetMovieError = HTTPValidationError

export type GetMovieSessionsData = {
  body: MovieSessionsRequest
}

export type GetMovieSessionsResponse = Array<MovieSessionsResponse>

export type GetMovieSessionsError = HTTPValidationError

export type GetUserMeResponse = UserMeResponse

export type GetUserMeError = unknown

export type GetTicketsResponse = Array<UserTicketResponse>

export type GetTicketsError = unknown

export type GetTicketBySignData = {
  body: UserTicketSignRequest
}

export type GetTicketBySignResponse = UserTicketResponse

export type GetTicketBySignError = HTTPValidationError

export type ProcessPaymentData = {
  body: PaymentProcessRequest
}

export type ProcessPaymentResponse = PaymentProcessResponse

export type ProcessPaymentError = HTTPValidationError

export type GetAdminStatsResponse = AdminStatsResponse

export type GetAdminStatsError = unknown

export type GetUsersAdminData = {
  body?: AdminUserRequest | null
}

export type GetUsersAdminResponse = Array<UserMeResponse>

export type GetUsersAdminError = HTTPValidationError

export type SetUserAdminData = {
  body: AdminUserSetRequest
}

export type SetUserAdminResponse = unknown

export type SetUserAdminError = HTTPValidationError

export type DeleteMovieAdminData = {
  body: MovieRequest
}

export type DeleteMovieAdminResponse = unknown

export type DeleteMovieAdminError = HTTPValidationError

export type AddMovieAdminData = {
  body: MovieAddRequest
}

export type AddMovieAdminResponse = unknown

export type AddMovieAdminError = HTTPValidationError

export type GetSessionAdminData = {
  body: MoviesSessionsAdminRequest
}

export type GetSessionAdminResponse = Array<MovieSessionsResponse>

export type GetSessionAdminError = HTTPValidationError

export type DeleteSessionAdminData = {
  body: MovieSessionRequest
}

export type DeleteSessionAdminResponse = unknown

export type DeleteSessionAdminError = HTTPValidationError

export type AddSessionAdminData = {
  body: MovieSessionsAddRequest
}

export type AddSessionAdminResponse = unknown

export type AddSessionAdminError = HTTPValidationError

export type GetMoviesResponseTransformer = (
  data: any
) => Promise<GetMoviesResponse>

export type MovieResponseModelResponseTransformer = (data: any) => MovieResponse

export const MovieResponseModelResponseTransformer: MovieResponseModelResponseTransformer =
  (data) => {
    if (data?.create_time) {
      data.create_time = new Date(data.create_time)
    }
    if (data?.update_time) {
      data.update_time = new Date(data.update_time)
    }
    return data
  }

export const GetMoviesResponseTransformer: GetMoviesResponseTransformer =
  async (data) => {
    if (Array.isArray(data)) {
      data.forEach(MovieResponseModelResponseTransformer)
    }
    return data
  }

export type GetMovieResponseTransformer = (
  data: any
) => Promise<GetMovieResponse>

export const GetMovieResponseTransformer: GetMovieResponseTransformer = async (
  data
) => {
  MovieResponseModelResponseTransformer(data)
  return data
}

export type GetMovieSessionsResponseTransformer = (
  data: any
) => Promise<GetMovieSessionsResponse>

export type MovieSessionsResponseModelResponseTransformer = (
  data: any
) => MovieSessionsResponse

export const MovieSessionsResponseModelResponseTransformer: MovieSessionsResponseModelResponseTransformer =
  (data) => {
    if (data?.date) {
      data.date = new Date(data.date)
    }
    if (data?.create_time) {
      data.create_time = new Date(data.create_time)
    }
    if (data?.update_time) {
      data.update_time = new Date(data.update_time)
    }
    return data
  }

export const GetMovieSessionsResponseTransformer: GetMovieSessionsResponseTransformer =
  async (data) => {
    if (Array.isArray(data)) {
      data.forEach(MovieSessionsResponseModelResponseTransformer)
    }
    return data
  }

export type GetUserMeResponseTransformer = (
  data: any
) => Promise<GetUserMeResponse>

export type UserMeResponseModelResponseTransformer = (
  data: any
) => UserMeResponse

export const UserMeResponseModelResponseTransformer: UserMeResponseModelResponseTransformer =
  (data) => {
    if (data?.register_time) {
      data.register_time = new Date(data.register_time)
    }
    return data
  }

export const GetUserMeResponseTransformer: GetUserMeResponseTransformer =
  async (data) => {
    UserMeResponseModelResponseTransformer(data)
    return data
  }

export type GetTicketsResponseTransformer = (
  data: any
) => Promise<GetTicketsResponse>

export type UserTicketResponseModelResponseTransformer = (
  data: any
) => UserTicketResponse

export const UserTicketResponseModelResponseTransformer: UserTicketResponseModelResponseTransformer =
  (data) => {
    if (data?.film) {
      MovieResponseModelResponseTransformer(data.film)
    }
    if (data?.date) {
      data.date = new Date(data.date)
    }
    return data
  }

export const GetTicketsResponseTransformer: GetTicketsResponseTransformer =
  async (data) => {
    if (Array.isArray(data)) {
      data.forEach(UserTicketResponseModelResponseTransformer)
    }
    return data
  }

export type GetTicketBySignResponseTransformer = (
  data: any
) => Promise<GetTicketBySignResponse>

export const GetTicketBySignResponseTransformer: GetTicketBySignResponseTransformer =
  async (data) => {
    UserTicketResponseModelResponseTransformer(data)
    return data
  }

export type GetUsersAdminResponseTransformer = (
  data: any
) => Promise<GetUsersAdminResponse>

export const GetUsersAdminResponseTransformer: GetUsersAdminResponseTransformer =
  async (data) => {
    if (Array.isArray(data)) {
      data.forEach(UserMeResponseModelResponseTransformer)
    }
    return data
  }

export type GetSessionAdminResponseTransformer = (
  data: any
) => Promise<GetSessionAdminResponse>

export const GetSessionAdminResponseTransformer: GetSessionAdminResponseTransformer =
  async (data) => {
    if (Array.isArray(data)) {
      data.forEach(MovieSessionsResponseModelResponseTransformer)
    }
    return data
  }
