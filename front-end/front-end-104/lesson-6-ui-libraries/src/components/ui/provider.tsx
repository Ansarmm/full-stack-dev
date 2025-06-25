// src/components/ui/provider.tsx
import { ChakraProvider, createSystem, defaultConfig } from '@chakra-ui/react'
import { MantineProvider } from '@mantine/core'
import '@mantine/core/styles.css'
import { type ReactNode } from 'react'

// Create system instead of extendTheme
const system = createSystem(defaultConfig, {
  theme: {
    tokens: {
      colors: {
        // Add your custom colors here if needed
      }
    }
  }
})

interface ProviderProps {
  children: ReactNode
}

export function Provider({ children }: ProviderProps) {
  return (
    <MantineProvider>
      <ChakraProvider value={system}>
        {children}
      </ChakraProvider>
    </MantineProvider>
  )
}