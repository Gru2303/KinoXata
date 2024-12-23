// This file is auto-generated by @hey-api/openapi-ts

import {
  createClient,
  createConfig,
  type OptionsLegacyParser,
} from '@hey-api/client-axios'
import {
  type GetGoogleLoginUrlError,
  type GetGoogleLoginUrlResponse,
  type GoogleLoginCallbackData,
  type GoogleLoginCallbackError,
  type GoogleLoginCallbackResponse,
  type UnauthorizedError,
  type UnauthorizedResponse,
  type GetMoviesData,
  type GetMoviesError,
  type GetMoviesResponse,
  type GetMovieData,
  type GetMovieError,
  type GetMovieResponse,
  type GetMovieSessionsData,
  type GetMovieSessionsError,
  type GetMovieSessionsResponse,
  type GetUserMeError,
  type GetUserMeResponse,
  type GetTicketsError,
  type GetTicketsResponse,
  type GetTicketBySignData,
  type GetTicketBySignError,
  type GetTicketBySignResponse,
  type ProcessPaymentData,
  type ProcessPaymentError,
  type ProcessPaymentResponse,
  type GetAdminStatsError,
  type GetAdminStatsResponse,
  type GetUsersAdminData,
  type GetUsersAdminError,
  type GetUsersAdminResponse,
  type SetUserAdminData,
  type SetUserAdminError,
  type SetUserAdminResponse,
  type DeleteMovieAdminData,
  type DeleteMovieAdminError,
  type DeleteMovieAdminResponse,
  type AddMovieAdminData,
  type AddMovieAdminError,
  type AddMovieAdminResponse,
  type GetSessionAdminData,
  type GetSessionAdminError,
  type GetSessionAdminResponse,
  type DeleteSessionAdminData,
  type DeleteSessionAdminError,
  type DeleteSessionAdminResponse,
  type AddSessionAdminData,
  type AddSessionAdminError,
  type AddSessionAdminResponse,
  GetMoviesResponseTransformer,
  GetMovieResponseTransformer,
  GetMovieSessionsResponseTransformer,
  GetUserMeResponseTransformer,
  GetTicketsResponseTransformer,
  GetTicketBySignResponseTransformer,
  GetUsersAdminResponseTransformer,
  GetSessionAdminResponseTransformer,
} from './types.gen'

export const client = createClient(createConfig())

/**
 * Get Google Login Url
 */
export const getGoogleLoginUrl = <ThrowOnError extends boolean = false>(
  options?: OptionsLegacyParser<unknown, ThrowOnError>
) => {
  return (options?.client ?? client).get<
    GetGoogleLoginUrlResponse,
    GetGoogleLoginUrlError,
    ThrowOnError
  >({
    ...options,
    url: '/api/v1/login/google/',
  })
}

/**
 * Get Google Login Url
 */
export const googleLoginCallback = <ThrowOnError extends boolean = false>(
  options?: OptionsLegacyParser<GoogleLoginCallbackData, ThrowOnError>
) => {
  return (options?.client ?? client).get<
    GoogleLoginCallbackResponse,
    GoogleLoginCallbackError,
    ThrowOnError
  >({
    ...options,
    url: '/api/v1/login/google/callback',
  })
}

/**
 * Unauthorized
 */
export const unauthorized = <ThrowOnError extends boolean = false>(
  options?: OptionsLegacyParser<unknown, ThrowOnError>
) => {
  return (options?.client ?? client).post<
    UnauthorizedResponse,
    UnauthorizedError,
    ThrowOnError
  >({
    ...options,
    url: '/api/v1/login/unauthorized',
  })
}

/**
 * Get All Movies
 */
export const getMovies = <ThrowOnError extends boolean = false>(
  options?: OptionsLegacyParser<GetMoviesData, ThrowOnError>
) => {
  return (options?.client ?? client).post<
    GetMoviesResponse,
    GetMoviesError,
    ThrowOnError
  >({
    ...options,
    url: '/api/v1/movies/all',
    responseTransformer: GetMoviesResponseTransformer,
  })
}

/**
 * Get All Movies
 */
export const getMovie = <ThrowOnError extends boolean = false>(
  options: OptionsLegacyParser<GetMovieData, ThrowOnError>
) => {
  return (options?.client ?? client).post<
    GetMovieResponse,
    GetMovieError,
    ThrowOnError
  >({
    ...options,
    url: '/api/v1/movies/movie',
    responseTransformer: GetMovieResponseTransformer,
  })
}

/**
 * Get All Movies
 */
export const getMovieSessions = <ThrowOnError extends boolean = false>(
  options: OptionsLegacyParser<GetMovieSessionsData, ThrowOnError>
) => {
  return (options?.client ?? client).post<
    GetMovieSessionsResponse,
    GetMovieSessionsError,
    ThrowOnError
  >({
    ...options,
    url: '/api/v1/movies/movie/sessions',
    responseTransformer: GetMovieSessionsResponseTransformer,
  })
}

/**
 * Me
 */
export const getUserMe = <ThrowOnError extends boolean = false>(
  options?: OptionsLegacyParser<unknown, ThrowOnError>
) => {
  return (options?.client ?? client).get<
    GetUserMeResponse,
    GetUserMeError,
    ThrowOnError
  >({
    ...options,
    url: '/api/v1/user/me',
    responseTransformer: GetUserMeResponseTransformer,
  })
}

/**
 * Get Tickets
 */
export const getTickets = <ThrowOnError extends boolean = false>(
  options?: OptionsLegacyParser<unknown, ThrowOnError>
) => {
  return (options?.client ?? client).get<
    GetTicketsResponse,
    GetTicketsError,
    ThrowOnError
  >({
    ...options,
    url: '/api/v1/user/tickets',
    responseTransformer: GetTicketsResponseTransformer,
  })
}

/**
 * Get Ticket By Sign Request
 */
export const getTicketBySign = <ThrowOnError extends boolean = false>(
  options: OptionsLegacyParser<GetTicketBySignData, ThrowOnError>
) => {
  return (options?.client ?? client).post<
    GetTicketBySignResponse,
    GetTicketBySignError,
    ThrowOnError
  >({
    ...options,
    url: '/api/v1/user/ticket/sign',
    responseTransformer: GetTicketBySignResponseTransformer,
  })
}

/**
 * Process Payment
 */
export const processPayment = <ThrowOnError extends boolean = false>(
  options: OptionsLegacyParser<ProcessPaymentData, ThrowOnError>
) => {
  return (options?.client ?? client).post<
    ProcessPaymentResponse,
    ProcessPaymentError,
    ThrowOnError
  >({
    ...options,
    url: '/api/v1/payment/',
  })
}

/**
 * Get Admin Stats
 */
export const getAdminStats = <ThrowOnError extends boolean = false>(
  options?: OptionsLegacyParser<unknown, ThrowOnError>
) => {
  return (options?.client ?? client).get<
    GetAdminStatsResponse,
    GetAdminStatsError,
    ThrowOnError
  >({
    ...options,
    url: '/api/v1/admin/stats',
  })
}

/**
 * Get Users Admin
 */
export const getUsersAdmin = <ThrowOnError extends boolean = false>(
  options?: OptionsLegacyParser<GetUsersAdminData, ThrowOnError>
) => {
  return (options?.client ?? client).post<
    GetUsersAdminResponse,
    GetUsersAdminError,
    ThrowOnError
  >({
    ...options,
    url: '/api/v1/admin/users',
    responseTransformer: GetUsersAdminResponseTransformer,
  })
}

/**
 * Get Users Admin
 */
export const setUserAdmin = <ThrowOnError extends boolean = false>(
  options: OptionsLegacyParser<SetUserAdminData, ThrowOnError>
) => {
  return (options?.client ?? client).post<
    SetUserAdminResponse,
    SetUserAdminError,
    ThrowOnError
  >({
    ...options,
    url: '/api/v1/admin/users/set',
  })
}

/**
 * Film Delete Admin
 */
export const deleteMovieAdmin = <ThrowOnError extends boolean = false>(
  options: OptionsLegacyParser<DeleteMovieAdminData, ThrowOnError>
) => {
  return (options?.client ?? client).post<
    DeleteMovieAdminResponse,
    DeleteMovieAdminError,
    ThrowOnError
  >({
    ...options,
    url: '/api/v1/admin/films/delete',
  })
}

/**
 * Film Add Admin
 */
export const addMovieAdmin = <ThrowOnError extends boolean = false>(
  options: OptionsLegacyParser<AddMovieAdminData, ThrowOnError>
) => {
  return (options?.client ?? client).post<
    AddMovieAdminResponse,
    AddMovieAdminError,
    ThrowOnError
  >({
    ...options,
    url: '/api/v1/admin/films/add',
  })
}

/**
 * Get Session Admin
 */
export const getSessionAdmin = <ThrowOnError extends boolean = false>(
  options: OptionsLegacyParser<GetSessionAdminData, ThrowOnError>
) => {
  return (options?.client ?? client).post<
    GetSessionAdminResponse,
    GetSessionAdminError,
    ThrowOnError
  >({
    ...options,
    url: '/api/v1/admin/sessions',
    responseTransformer: GetSessionAdminResponseTransformer,
  })
}

/**
 * Delete Session Admin
 */
export const deleteSessionAdmin = <ThrowOnError extends boolean = false>(
  options: OptionsLegacyParser<DeleteSessionAdminData, ThrowOnError>
) => {
  return (options?.client ?? client).post<
    DeleteSessionAdminResponse,
    DeleteSessionAdminError,
    ThrowOnError
  >({
    ...options,
    url: '/api/v1/admin/sessions/delete',
  })
}

/**
 * Add Session Admin
 */
export const addSessionAdmin = <ThrowOnError extends boolean = false>(
  options: OptionsLegacyParser<AddSessionAdminData, ThrowOnError>
) => {
  return (options?.client ?? client).post<
    AddSessionAdminResponse,
    AddSessionAdminError,
    ThrowOnError
  >({
    ...options,
    url: '/api/v1/admin/sessions/add',
  })
}
