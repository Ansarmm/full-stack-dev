import { Button, Box, Heading, Text, Badge } from '@chakra-ui/react';
import { Calendar } from "@/components/ui/calendar"
import React from "react"
import {
  Carousel,
  CarouselContent,
  CarouselItem,
  CarouselNext,
  CarouselPrevious,
} from "@/components/ui/carousel"
import { Checkbox } from "@/components/ui/checkbox"
import { Label } from "@/components/ui/label"

function ChakraDemo() {
  return (
    <div>
      <h2>Chakra UI Компоненты</h2>

      <Button colorScheme="blue">Кнопка Chakra</Button>

      <Box maxW="sm" borderWidth="1px" borderRadius="lg" overflow="hidden" mt="20px">
        <img src="https://via.placeholder.com/150" alt="Demo Image" />
        <Box p="6">
          <Box display="flex" alignItems="baseline">
            <Badge borderRadius="full" px="2" colorScheme="teal">Новинка</Badge>
          </Box>
          <Heading mt="1" size="md" fontWeight="semibold">Заголовок карточки</Heading>
          <Text mt="2" color="gray.500">Описание карточки Chakra UI</Text>
        </Box>
      </Box>
    </div>
  );
}

export function CheckboxDemo() {
  return (
    <div className="flex flex-col gap-6">
      <div className="flex items-center gap-3">
        <Checkbox id="terms" />
        <Label htmlFor="terms">Accept terms and conditions</Label>
      </div>
      <div className="flex items-start gap-3">
        <Checkbox id="terms-2" defaultChecked />
        <div className="grid gap-2">
          <Label htmlFor="terms-2">Accept terms and conditions</Label>
          <p className="text-muted-foreground text-sm">
            By clicking this checkbox, you agree to the terms and conditions.
          </p>
        </div>
      </div>
      <div className="flex items-start gap-3">
        <Checkbox id="toggle" disabled />
        <Label htmlFor="toggle">Enable notifications</Label>
      </div>
      <Label className="hover:bg-accent/50 flex items-start gap-3 rounded-lg border p-3 has-[[aria-checked=true]]:border-blue-600 has-[[aria-checked=true]]:bg-blue-50 dark:has-[[aria-checked=true]]:border-blue-900 dark:has-[[aria-checked=true]]:bg-blue-950">
        <Checkbox
          id="toggle-2"
          defaultChecked
          className="data-[state=checked]:border-blue-600 data-[state=checked]:bg-blue-600 data-[state=checked]:text-white dark:data-[state=checked]:border-blue-700 dark:data-[state=checked]:bg-blue-700"
        />
        <div className="grid gap-1.5 font-normal">
          <p className="text-sm leading-none font-medium">
            Enable notifications
          </p>
          <p className="text-muted-foreground text-sm">
            You can enable or disable notifications at any time.
          </p>
        </div>
      </Label>
    </div>
  )
}
function ShadcnDemo() {
    const [date, setDate] = React.useState<Date | undefined>(new Date())
 
    return (
      <>
        <Calendar
          mode="single"
          selected={date}
          onSelect={setDate}
          className="rounded-lg border"
        />

        <Carousel>
          <CarouselContent>
            <CarouselItem>1</CarouselItem>
            <CarouselItem>2</CarouselItem>
            <CarouselItem>3</CarouselItem>
          </CarouselContent>
          <CarouselPrevious />
          <CarouselNext />
        </Carousel>
        <CheckboxDemo />
      </>
    )
}

function App() {
  return (
    <>
      <ChakraDemo />
      <ShadcnDemo />
    </>
  )
}

export default App;