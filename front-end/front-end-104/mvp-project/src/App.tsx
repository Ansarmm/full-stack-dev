import { useQuery } from '@tanstack/react-query'
import axios from 'axios'
import { Button, HStack, Box, Text, Link} from "@chakra-ui/react"

function App() {
  const { data } = useQuery({
    queryKey: ['todo'],
    queryFn: () => axios.get('https://jsonplaceholder.typicode.com/posts')
      .then(response => response.data)
  })

  return (
    <Box>
      <Link 
        href="index.html" 
        color="white" 
        _hover={{ textDecoration: "underline" }}
      >
        Home page
      </Link>
      <Text fontSize="3xl" color="blue.500" m={4}>Projects:</Text>
      
      {data && <Text m={4}>Todo: {data.title}</Text>}
      
      <HStack m={4}>
        <Button colorScheme="blue">Click me</Button>
      </HStack>
    </Box>
  )
}

export default App