/** @type {import('next').NextConfig} */
const nextConfig = {
  reactStrictMode: true,
}

module.exports = nextConfig


// module.exports = (phase, {defaultConfig}) => {
//   if ('sassOptions' in defaultConfig) {
//       defaultConfig['sassOptions'] = {
//           includePaths: ['./src'],
//           prependData: `@import "~@styles/theme.scss";`,
//       }
//   }
//   return defaultConfig;
// }