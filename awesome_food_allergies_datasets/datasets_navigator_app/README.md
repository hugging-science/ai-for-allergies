# Datasets Navigator

A modern web application for navigating and exploring food allergy datasets, built with Next.js 14, React, TypeScript, and Tailwind CSS.

## Prerequisites

- [Node.js](https://nodejs.org/) (v18 or higher)
- [pnpm](https://pnpm.io/) (v8 or higher)

If you don't have pnpm installed, you can install it with:
```bash
npm install -g pnpm
```

## Getting Started

### Installation

Install all dependencies:

```bash
pnpm install
```

### Development

Run the development server:

```bash
pnpm dev
```

Open [http://localhost:3000](http://localhost:3000) with your browser to see the result.

The application will automatically reload when you make changes to the source files.

### Building for Production

Create an optimized production build:

```bash
pnpm build
```

Start the production server:

```bash
pnpm start
```

### Linting

Run the linter to check for code quality issues:

```bash
pnpm lint
```

## Tech Stack

- **Framework:** [Next.js 14](https://nextjs.org/) with App Router
- **Language:** [TypeScript](https://www.typescriptlang.org/)
- **Styling:** [Tailwind CSS](https://tailwindcss.com/)
- **UI Components:** [Radix UI](https://www.radix-ui.com/)
- **Icons:** [Lucide React](https://lucide.dev/)
- **Charts:** [Recharts](https://recharts.org/)
- **Forms:** [React Hook Form](https://react-hook-form.com/) with [Zod](https://zod.dev/)

## Project Structure

```
datasets_navigator/
├── app/              # Next.js App Router pages
├── components/       # React components
│   └── ui/          # Reusable UI components
├── hooks/           # Custom React hooks
├── lib/             # Utility functions
├── public/          # Static assets
└── styles/          # Global styles
```

## Features

- Interactive dataset exploration interface
- Modern, responsive design
- Dark/light theme support
- Component-based architecture
- Type-safe with TypeScript

## Contributing

1. Make your changes in a feature branch
2. Run `pnpm lint` to ensure code quality
3. Test your changes with `pnpm dev`
4. Submit a pull request

## License

See the [LICENSE](../../LICENSE) file for details.

