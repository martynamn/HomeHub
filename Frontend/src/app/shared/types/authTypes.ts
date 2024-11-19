export interface KeyCloakTokenResult {
  success: boolean;
  token: string | undefined;
}

export interface KeyCloakConstructorParams {
  url: string;
  realm: string;
  clientId: string;
  'ssl-required': 'external';
  'public-client': boolean;
  resource: string;
  'auth-server-url': string;
  'confidential-port': number;
  logoutUrl: string;
  redirect_uri: string;
}

export interface TokenParsed {
  acr: string
  aud: string
  auth_time: number
  azp: string
  email: string
  email_verified: true
  exp: number
  family_name: string
  given_name: string
  iat: number
  iss: string
  jti: string
  name: string
  nonce: string
  preferred_username: string
  scope: string
  session_state: string
  sid: string
  sub: string
  typ: string
}