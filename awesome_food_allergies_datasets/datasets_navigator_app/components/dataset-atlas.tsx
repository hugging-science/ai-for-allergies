"use client"

import { useState, useMemo, useEffect } from "react"
import { Search, ExternalLink, Mail, FileText, X, ChevronDown } from "lucide-react"
import { Input } from "@/components/ui/input"
import { Badge } from "@/components/ui/badge"
import { Card, CardContent, CardDescription, CardFooter, CardHeader, CardTitle } from "@/components/ui/card"
import { Button } from "@/components/ui/button"
import {
  DropdownMenu,
  DropdownMenuContent,
  DropdownMenuCheckboxItem,
  DropdownMenuTrigger,
} from "@/components/ui/dropdown-menu"
import { Dialog, DialogContent, DialogDescription, DialogHeader, DialogTitle } from "@/components/ui/dialog"

interface Dataset {
  Name: string
  Category: string
  Description: string
  Task: string
  Data_Type: string
  Source: string
  "Paper link": string
  Availability: string
  Contact: string
}

function getCategoryColor(category: string): { bg: string; text: string } {
  const colors = [
    { bg: "bg-blue-100 dark:bg-blue-950", text: "text-blue-700 dark:text-blue-300" },
    { bg: "bg-emerald-100 dark:bg-emerald-950", text: "text-emerald-700 dark:text-emerald-300" },
    { bg: "bg-amber-100 dark:bg-amber-950", text: "text-amber-700 dark:text-amber-300" },
    { bg: "bg-rose-100 dark:bg-rose-950", text: "text-rose-700 dark:text-rose-300" },
    { bg: "bg-cyan-100 dark:bg-cyan-950", text: "text-cyan-700 dark:text-cyan-300" },
  ]
  const hash = category.split("").reduce((acc, char) => acc + char.charCodeAt(0), 0)
  return colors[hash % colors.length]
}

function getDataTypeColor(dataType: string): { bg: string; text: string } {
  const colors = [
    { bg: "bg-indigo-100 dark:bg-indigo-950", text: "text-indigo-700 dark:text-indigo-300" },
    { bg: "bg-teal-100 dark:bg-teal-950", text: "text-teal-700 dark:text-teal-300" },
    { bg: "bg-orange-100 dark:bg-orange-950", text: "text-orange-700 dark:text-orange-300" },
    { bg: "bg-pink-100 dark:bg-pink-950", text: "text-pink-700 dark:text-pink-300" },
    { bg: "bg-lime-100 dark:bg-lime-950", text: "text-lime-700 dark:text-lime-300" },
    { bg: "bg-sky-100 dark:bg-sky-950", text: "text-sky-700 dark:text-sky-300" },
  ]
  const hash = dataType.split("").reduce((acc, char) => acc + char.charCodeAt(0), 0)
  return colors[hash % colors.length]
}

export function DatasetAtlas() {
  const [datasets, setDatasets] = useState<Dataset[]>([])
  const [searchQuery, setSearchQuery] = useState("")
  const [selectedCategory, setSelectedCategory] = useState<string>("all")
  const [selectedTasks, setSelectedTasks] = useState<string[]>([])
  const [selectedDataTypes, setSelectedDataTypes] = useState<string[]>([])
  const [loading, setLoading] = useState(true)
  const [selectedDataset, setSelectedDataset] = useState<Dataset | null>(null)

  useEffect(() => {
    async function fetchData() {
      try {
        const response = await fetch(
          "https://blobs.vusercontent.net/blob/Awesome%20food%20allergy%20datasets%20-%20Copia%20di%20Full%20view%20%281%29-nbq61oXBgltNRiIJIq8djoMoqX7ItK.tsv",
        )
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`)
        }
        const text = await response.text()
        console.log("[v0] TSV text length:", text.length)
        const parsed = parseTSV(text)
        console.log("[v0] Parsed datasets count:", parsed.length)
        console.log("[v0] First dataset:", parsed[0])
        setDatasets(parsed)
      } catch (error) {
        console.error("[v0] Error fetching datasets:", error)
      } finally {
        setLoading(false)
      }
    }
    fetchData()
  }, [])

  function parseTSV(text: string): Dataset[] {
    const lines = text.split("\n")
    const headers = lines[0].split("\t").map((h) => h.trim().replace(/^"|"$/g, ""))

    return lines
      .slice(1)
      .filter((line) => line.trim())
      .map((line) => {
        const values = line.split("\t").map((v) => v.trim())
        const dataset: any = {}
        headers.forEach((header, index) => {
          dataset[header] = values[index] || ""
        })
        return dataset as Dataset
      })
  }

  const categories = useMemo(() => {
    const cats = new Set(datasets.map((d) => d.Category).filter(Boolean))
    return ["all", ...Array.from(cats).sort()]
  }, [datasets])

  const tasks = useMemo(() => {
    const taskSet = new Set<string>()
    datasets.forEach((dataset) => {
      if (dataset.Task) {
        const individualTasks = dataset.Task.split(",").map((task) => task.trim())
        individualTasks.forEach((task) => {
          if (task) taskSet.add(task)
        })
      }
    })
    return Array.from(taskSet).sort()
  }, [datasets])

  const dataTypes = useMemo(() => {
    const typeSet = new Set(datasets.map((d) => d.Data_Type).filter(Boolean))
    return Array.from(typeSet).sort()
  }, [datasets])

  const filteredDatasets = useMemo(() => {
    return datasets.filter((dataset) => {
      const matchesSearch =
        dataset.Name?.toLowerCase().includes(searchQuery.toLowerCase()) ||
        dataset.Description?.toLowerCase().includes(searchQuery.toLowerCase()) ||
        dataset.Category?.toLowerCase().includes(searchQuery.toLowerCase()) ||
        dataset.Task?.toLowerCase().includes(searchQuery.toLowerCase()) ||
        dataset.Data_Type?.toLowerCase().includes(searchQuery.toLowerCase())

      const matchesCategory = selectedCategory === "all" || dataset.Category === selectedCategory

      const matchesTask =
        selectedTasks.length === 0 ||
        dataset.Task.split(",")
          .map((t) => t.trim())
          .some((task) => selectedTasks.includes(task))

      const matchesDataType = selectedDataTypes.length === 0 || selectedDataTypes.includes(dataset.Data_Type)

      return matchesSearch && matchesCategory && matchesTask && matchesDataType
    })
  }, [datasets, searchQuery, selectedCategory, selectedTasks, selectedDataTypes])

  const toggleTask = (task: string) => {
    setSelectedTasks((prev) => (prev.includes(task) ? prev.filter((t) => t !== task) : [...prev, task]))
  }

  const removeTask = (task: string) => {
    setSelectedTasks((prev) => prev.filter((t) => t !== task))
  }

  const clearAllTasks = () => {
    setSelectedTasks([])
  }

  const toggleDataType = (dataType: string) => {
    setSelectedDataTypes((prev) => (prev.includes(dataType) ? prev.filter((t) => t !== dataType) : [...prev, dataType]))
  }

  const removeDataType = (dataType: string) => {
    setSelectedDataTypes((prev) => prev.filter((t) => t !== dataType))
  }

  const clearAllDataTypes = () => {
    setSelectedDataTypes([])
  }

  return (
    <div className="min-h-screen bg-background">
      {/* Header */}
      <header className="border-b border-border bg-card">
        <div className="container mx-auto px-4 py-6 md:py-8">
          <h1 className="text-3xl md:text-4xl font-bold text-balance mb-2">Food Allergy Research Dataset Atlas</h1>
          <p className="text-muted-foreground text-lg text-pretty">
            A curated collection of datasets for advancing food allergy research
          </p>
        </div>
      </header>

      <div className="container mx-auto px-4 py-8">
        {/* Search and Filters */}
        <div className="mb-8 space-y-4">
          <div className="relative">
            <Search className="absolute left-3 top-1/2 -translate-y-1/2 h-5 w-5 text-muted-foreground" />
            <Input
              type="text"
              placeholder="Search datasets by name, description, category, task, or data type..."
              value={searchQuery}
              onChange={(e) => setSearchQuery(e.target.value)}
              className="pl-10 h-12 text-base"
            />
          </div>

          <div className="flex flex-col gap-4">
            <div>
              <label className="text-sm font-medium mb-2 block">Filter by Category</label>
              <div className="flex flex-wrap gap-2">
                {categories.map((category) => (
                  <Button
                    key={category}
                    variant={selectedCategory === category ? "default" : "outline"}
                    size="sm"
                    onClick={() => setSelectedCategory(category)}
                    className="capitalize"
                  >
                    {category}
                  </Button>
                ))}
              </div>
            </div>

            <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
              <div>
                <label className="text-sm font-medium mb-2 block">Filter by Task</label>
                <div className="space-y-2">
                  <DropdownMenu>
                    <DropdownMenuTrigger asChild>
                      <Button variant="outline" className="w-full justify-between bg-transparent">
                        <span>
                          {selectedTasks.length === 0
                            ? "Select tasks..."
                            : `${selectedTasks.length} task${selectedTasks.length > 1 ? "s" : ""} selected`}
                        </span>
                        <ChevronDown className="h-4 w-4 opacity-50" />
                      </Button>
                    </DropdownMenuTrigger>
                    <DropdownMenuContent className="w-[300px] max-h-[300px] overflow-y-auto">
                      {tasks.map((task) => (
                        <DropdownMenuCheckboxItem
                          key={task}
                          checked={selectedTasks.includes(task)}
                          onCheckedChange={() => toggleTask(task)}
                        >
                          {task}
                        </DropdownMenuCheckboxItem>
                      ))}
                    </DropdownMenuContent>
                  </DropdownMenu>

                  {selectedTasks.length > 0 && (
                    <div className="flex flex-wrap gap-2">
                      {selectedTasks.map((task) => (
                        <Badge key={task} variant="secondary" className="pl-2 pr-1 py-1 text-xs shadow-none">
                          {task}
                          <button onClick={() => removeTask(task)} className="ml-1 hover:bg-muted rounded-full p-0.5">
                            <X className="h-3 w-3" />
                          </button>
                        </Badge>
                      ))}
                      <Button variant="ghost" size="sm" onClick={clearAllTasks} className="h-6 px-2 text-xs">
                        Clear all
                      </Button>
                    </div>
                  )}
                </div>
              </div>

              <div>
                <label className="text-sm font-medium mb-2 block">Filter by Data Type</label>
                <div className="space-y-2">
                  <DropdownMenu>
                    <DropdownMenuTrigger asChild>
                      <Button variant="outline" className="w-full justify-between bg-transparent">
                        <span>
                          {selectedDataTypes.length === 0
                            ? "Select data types..."
                            : `${selectedDataTypes.length} type${selectedDataTypes.length > 1 ? "s" : ""} selected`}
                        </span>
                        <ChevronDown className="h-4 w-4 opacity-50" />
                      </Button>
                    </DropdownMenuTrigger>
                    <DropdownMenuContent className="w-[300px] max-h-[300px] overflow-y-auto">
                      {dataTypes.map((dataType) => (
                        <DropdownMenuCheckboxItem
                          key={dataType}
                          checked={selectedDataTypes.includes(dataType)}
                          onCheckedChange={() => toggleDataType(dataType)}
                        >
                          {dataType}
                        </DropdownMenuCheckboxItem>
                      ))}
                    </DropdownMenuContent>
                  </DropdownMenu>

                  {selectedDataTypes.length > 0 && (
                    <div className="flex flex-wrap gap-2">
                      {selectedDataTypes.map((dataType) => (
                        <Badge key={dataType} variant="secondary" className="pl-2 pr-1 py-1 text-xs shadow-none">
                          {dataType}
                          <button
                            onClick={() => removeDataType(dataType)}
                            className="ml-1 hover:bg-muted rounded-full p-0.5"
                          >
                            <X className="h-3 w-3" />
                          </button>
                        </Badge>
                      ))}
                      <Button variant="ghost" size="sm" onClick={clearAllDataTypes} className="h-6 px-2 text-xs">
                        Clear all
                      </Button>
                    </div>
                  )}
                </div>
              </div>
            </div>
          </div>
        </div>

        {/* Results Count */}
        <div className="mb-6">
          <p className="text-sm text-muted-foreground">
            Showing <span className="font-semibold text-foreground">{filteredDatasets.length}</span> of{" "}
            <span className="font-semibold text-foreground">{datasets.length}</span> datasets
          </p>
        </div>

        {/* Dataset Grid */}
        {loading ? (
          <div className="text-center py-12">
            <p className="text-muted-foreground">Loading datasets...</p>
          </div>
        ) : filteredDatasets.length === 0 ? (
          <div className="text-center py-12">
            <p className="text-muted-foreground">No datasets found matching your criteria.</p>
          </div>
        ) : (
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
            {filteredDatasets.map((dataset, index) => {
              const categoryColors = getCategoryColor(dataset.Category)
              const dataTypeColors = getDataTypeColor(dataset.Data_Type)
              return (
                <Card
                  key={index}
                  className="flex flex-col hover:shadow-lg transition-shadow cursor-pointer h-[480px]"
                  onClick={() => setSelectedDataset(dataset)}
                >
                  <CardHeader className="pb-3">
                    <div className="flex gap-2 mb-3 flex-wrap">
                      {dataset.Category && (
                        <Badge className={`text-xs border-0 shadow-none ${categoryColors.bg} ${categoryColors.text}`}>
                          {dataset.Category}
                        </Badge>
                      )}
                      {dataset.Data_Type && (
                        <Badge className={`text-xs border-0 shadow-none ${dataTypeColors.bg} ${dataTypeColors.text}`}>
                          {dataset.Data_Type}
                        </Badge>
                      )}
                      {dataset.Availability && (
                        <Badge
                          variant={dataset.Availability.toLowerCase().includes("open") ? "default" : "outline"}
                          className="text-xs shadow-none"
                        >
                          {dataset.Availability}
                        </Badge>
                      )}
                    </div>
                    <CardTitle className="text-xl text-balance leading-tight">{dataset.Name}</CardTitle>
                    {dataset.Task && (
                      <CardDescription className="text-sm font-medium line-clamp-2">
                        Task: {dataset.Task}
                      </CardDescription>
                    )}
                  </CardHeader>
                  <CardContent className="flex-1 pb-3">
                    <p className="text-sm text-muted-foreground text-pretty leading-relaxed line-clamp-4">
                      {dataset.Description}
                    </p>
                  </CardContent>
                  <CardFooter className="flex flex-col gap-2 items-stretch pt-3 pb-5">
                    {dataset.Source && (
                      <Button
                        variant="default"
                        size="sm"
                        asChild
                        className="w-full"
                        onClick={(e) => e.stopPropagation()}
                      >
                        <a href={dataset.Source} target="_blank" rel="noopener noreferrer">
                          <ExternalLink className="h-4 w-4 mr-2" />
                          Access Dataset
                        </a>
                      </Button>
                    )}
                    <div className="flex gap-2">
                      {dataset["Paper link"] && (
                        <Button
                          variant="outline"
                          size="sm"
                          asChild
                          className="flex-1 bg-transparent"
                          onClick={(e) => e.stopPropagation()}
                        >
                          <a href={dataset["Paper link"]} target="_blank" rel="noopener noreferrer">
                            <FileText className="h-4 w-4 mr-2" />
                            Paper
                          </a>
                        </Button>
                      )}
                      {dataset.Contact && (
                        <Button
                          variant="outline"
                          size="sm"
                          asChild
                          className="flex-1 bg-transparent"
                          onClick={(e) => e.stopPropagation()}
                        >
                          <a href={`mailto:${dataset.Contact}`}>
                            <Mail className="h-4 w-4 mr-2" />
                            Contact
                          </a>
                        </Button>
                      )}
                    </div>
                  </CardFooter>
                </Card>
              )
            })}
          </div>
        )}
      </div>

      {/* Modal Dialog for Expanded Dataset View */}
      <Dialog open={!!selectedDataset} onOpenChange={(open) => !open && setSelectedDataset(null)}>
        <DialogContent className="max-w-2xl max-h-[80vh] overflow-y-auto">
          {selectedDataset && (
            <>
              <DialogHeader>
                <div className="flex gap-2 mb-3 flex-wrap">
                  {selectedDataset.Category && (
                    <Badge
                      className={`text-xs border-0 shadow-none ${getCategoryColor(selectedDataset.Category).bg} ${getCategoryColor(selectedDataset.Category).text}`}
                    >
                      {selectedDataset.Category}
                    </Badge>
                  )}
                  {selectedDataset.Data_Type && (
                    <Badge
                      className={`text-xs border-0 shadow-none ${getDataTypeColor(selectedDataset.Data_Type).bg} ${getDataTypeColor(selectedDataset.Data_Type).text}`}
                    >
                      {selectedDataset.Data_Type}
                    </Badge>
                  )}
                  {selectedDataset.Availability && (
                    <Badge
                      variant={selectedDataset.Availability.toLowerCase().includes("open") ? "default" : "outline"}
                      className="text-xs shadow-none"
                    >
                      {selectedDataset.Availability}
                    </Badge>
                  )}
                </div>
                <DialogTitle className="text-2xl text-balance">{selectedDataset.Name}</DialogTitle>
                {selectedDataset.Task && (
                  <DialogDescription className="text-base font-medium text-foreground">
                    Task: {selectedDataset.Task}
                  </DialogDescription>
                )}
              </DialogHeader>
              <div className="space-y-6 mt-4">
                <div>
                  <h3 className="font-semibold mb-2 text-sm uppercase tracking-wide text-muted-foreground">
                    Description
                  </h3>
                  <p className="text-sm leading-relaxed">{selectedDataset.Description}</p>
                </div>

                <div className="flex flex-col gap-3">
                  {selectedDataset.Source && (
                    <Button variant="default" size="default" asChild className="w-full">
                      <a href={selectedDataset.Source} target="_blank" rel="noopener noreferrer">
                        <ExternalLink className="h-4 w-4 mr-2" />
                        Access Dataset
                      </a>
                    </Button>
                  )}
                  <div className="flex gap-3">
                    {selectedDataset["Paper link"] && (
                      <Button variant="outline" size="default" asChild className="flex-1 bg-transparent">
                        <a href={selectedDataset["Paper link"]} target="_blank" rel="noopener noreferrer">
                          <FileText className="h-4 w-4 mr-2" />
                          Read Paper
                        </a>
                      </Button>
                    )}
                    {selectedDataset.Contact && (
                      <Button variant="outline" size="default" asChild className="flex-1 bg-transparent">
                        <a href={`mailto:${selectedDataset.Contact}`}>
                          <Mail className="h-4 w-4 mr-2" />
                          Contact
                        </a>
                      </Button>
                    )}
                  </div>
                </div>
              </div>
            </>
          )}
        </DialogContent>
      </Dialog>
    </div>
  )
}
